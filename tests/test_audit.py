import tempfile
import unittest
from pathlib import Path
from cron_expression_description_claim_audit.audit import audit, claims, evidence, main
from cron_expression_description_claim_audit.phrases import CRONEXPRESSIONDESCRIPTION, NOCRONEXPRESSIONDESCRIPTION, GENERIC_NAMES

class AuditTests(unittest.TestCase):
    def test_phrases(self):
        for phrase in CRONEXPRESSIONDESCRIPTION:
            with self.subTest(phrase=phrase): self.assertTrue(claims(phrase)[0])
        for phrase in NOCRONEXPRESSIONDESCRIPTION:
            with self.subTest(phrase=phrase): self.assertEqual((set(), {phrase}), claims(phrase))
        self.assertEqual((set(), set()), claims('```\ndescribe cron\n```'))

    def test_positive(self):
        routes=['import cron_descriptor as cd\ncd.get_description(x)', 'from cron_descriptor import get_description as f\nf(x)', 'from cron_descriptor.ExpressionDescriptor import get_description as f\nf(x)']
        for method in ('get_description','get_full_description'):
            routes += ['from cron_descriptor import ExpressionDescriptor as D\nD(x).'+method+'()', 'from cron_descriptor import ExpressionDescriptor as D\nd=D(x)\nd.'+method+'()', 'import cron_descriptor as cd\ncd.ExpressionDescriptor.'+method+'(d)']
        for method in ('str','repr'):
            routes += ['from cron_descriptor import ExpressionDescriptor as D\n'+method+'(D(x))', 'from cron_descriptor import ExpressionDescriptor as D\nd=D(x)\n'+method+'(d)']
        routes += ['from crontab import CronItem as C\nC(x).description()', 'from crontab import CronItem as C\nc=C(x)\nc.description()', 'import crontab as ct\nct.CronItem.description(c)']
        for name in GENERIC_NAMES: routes += ['x.'+name+'()', 'from example import '+name+' as f\nf()']
        for code in routes:
            with self.subTest(code=code): self.assertTrue(evidence(code))

    def test_negative(self):
        routes=['import cron_descriptor','get_description(x)','x.get_description()','ExpressionDescriptor(x)','description(x)','x.description()','CronItem(x)','describe(x)','from cron_descriptor import ExpressionDescriptor as D\nD(x)','from cron_descriptor import Options\nOptions()', 'from cron_descriptor import ExpressionDescriptor as D\nf"{D(x)}"', 'from cron_descriptor import ExpressionDescriptor as D\nformat(D(x))','from crontab import CronItem\nCronItem(x).description','import subprocess\nsubprocess.run(["cron-descriptor"])','import cron_descriptor as cd\ncd=other\ncd.get_description(x)', 'def describe_cron(): pass\nx.describe_cron()']
        for method in ('get_time_of_day_description','get_seconds_description','get_minutes_description','get_hours_description','get_day_of_week_description','get_month_description','get_day_of_month_description','get_year_description','get_description_format','get_list_description','get_segment_description','generate_between_segment_description','format_time','number_to_day','get_ordinal','format_nth_days','translate'):
            routes.append('from cron_descriptor import ExpressionDescriptor as D\nD(x).'+method+'()')
        for method in ('is_valid','get_next','get_prev','match','match_range','expand'):
            routes.append('import croniter\ncroniter.'+method+'(x)')
        for method in ('parse','match_timestamp','match_datetime','get_execution_time'):
            routes.append('from cron_validator import CronValidator\nCronValidator.'+method+'(x)')
        for cls in ('CronTab','CronSlices','CronSlice','CronItem'):
            routes.append('from crontab import '+cls+'\nstr('+cls+'(x))')
        routes += ['from cronex import CronExpression\nCronExpression(x).check_trigger(x)','from cronex import CronExpression\nrepr(CronExpression(x))','from croniter import croniter\nstr(croniter(x))', 'def broken(:']
        for code in routes:
            with self.subTest(code=code): self.assertFalse(evidence(code))

    def test_findings(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); (p/'README.md').write_text('describe cron expression')
            self.assertEqual('HIGH',audit(p)[0]['severity'])
            (p/'test_a.py').write_text('import cron_descriptor\ncron_descriptor.get_description(x)')
            self.assertEqual('MEDIUM',audit(p)[0]['severity'])
            self.assertEqual(0,main(['audit',d])); self.assertEqual(2,main(['audit',d,'--fail-on','medium']))
            (p/'a.py').write_text('import cron_descriptor\ncron_descriptor.get_description(x)')
            self.assertFalse(audit(p)); (p/'README.md').write_text('no cron expression description')
            self.assertEqual('HIGH',audit(p)[0]['severity']); self.assertFalse(audit(p,['a.py']))

    def test_shadow(self):
        for code in ['from cron_descriptor import get_description\ndef get_description(x): pass\nget_description(x)', 'import cron_descriptor as cd\nwith x as cd: pass\ncd.get_description(x)', 'from cron_descriptor import ExpressionDescriptor as D\nD=other\nD(x).get_description()']:
            with self.subTest(code=code): self.assertFalse(evidence(code))

    def test_self(self):
        self.assertFalse(audit(Path(__file__).resolve().parents[1]))

if __name__ == '__main__': unittest.main()
