# Schedule-string claim audit

This offline tool checks documentation against Python source without executing the source. It reports unsupported positive claims and denials contradicted by production evidence.

```text
cron-expression-description-claim-audit
```

Install from a local distribution and run:

```sh
python3 -m pip install --no-cache-dir ./dist/*.whl
cron-expression-description-claim-audit audit .
python3 -m cron_expression_description_claim_audit audit . --json
```

Use `--fail-on medium` to include test-only evidence in the failure threshold. Repeat `--ignore PREFIX` to omit paths. `--verbose` shows matched text and evidence. Exit codes are 0 for pass, 2 for findings at the threshold, and 1 for usage or I/O errors.

```text
documented-cron-expression-description-claim-false
documented-no-cron-expression-description-claim-false
```

## Differentiation

Generic input checks determine whether input is checked at all.

ISBN checks judge book-number check digits.

ISSN checks judge serial-number check digits.

IBAN checks judge bank account numbers.

UUID checks judge identifier strings.

Semantic version checks judge version strings.

MAC address checks judge hardware addresses.

Scheduled execution runs jobs rather than judging schedule strings.

Date checks judge calendar dates.

Timeouts limit execution duration.

Schedule validation judges whether a string is well formed.

Payment processing takes a card payment.

Card extraction reads card details from documents.

Authentication can prove account ownership using codes or confirmation links.

Password verification compares a password with a stored hash.

Password hashing prepares a password for storage.

Password generation mints random passwords.

PDF encryption protects a file with a password.

Email sending delivers mail.

SMS sending delivers text messages.

Document extraction reads data from documents.

Barcode scanning decodes images.

Email checks judge address format or deliverability.

Phone checks judge number format or region.

Password strength checks judge password strength.

JSON Schema checks judge data against a schema.

Card checks judge number format, brand, and Luhn digits.

Domain checks judge host names.

URL checks judge web addresses.

IP checks judge numeric addresses.

JSON decoding produces a value.

Regular expressions match patterns.

URL parsing splits web addresses into parts.

Fetching retrieves a web address over a network.

DNS resolution looks up a name.

Barcode generation encodes account numbers.

Account-number extraction reads documents.

Next-run calculation uses a schedule.

Moment matching compares a time with a schedule.

Expansion produces field lists.

Parsing produces element objects.

A crontab file contains jobs and commands.

A single field is not an entire schedule string.

Schedule generation creates a new string.

The spreadsheet reading family is outside this tool.

The spreadsheet generation family is outside this tool.

The word-document reading family is outside this tool.

The word-document generation family is outside this tool.

The presentation reading family is outside this tool.

The presentation generation family is outside this tool.

The PDF extraction family is outside this tool.

The PDF generation family is outside this tool.

The PDF merging family is outside this tool.

The PDF splitting family is outside this tool.

The PDF rotation family is outside this tool.

The PDF form-filling family is outside this tool.

The PDF watermarking family is outside this tool.

The PDF redaction family is outside this tool.

The PDF compression family is outside this tool.

The PDF annotation family is outside this tool.

The table extraction family is outside this tool.

The OCR family is outside this tool.

The document extraction family is outside this tool.

The e-signature family is outside this tool.

The screen recording family is outside this tool.

The video generation family is outside this tool.

The QR code generation family is outside this tool.

The barcode generation family is outside this tool.

The barcode scanning family is outside this tool.

The audio mixing family is outside this tool.

The audio generation family is outside this tool.

The audio editing family is outside this tool.

The source separation family is outside this tool.

The speech recognition family is outside this tool.

The text-to-speech family is outside this tool.

The noise suppression family is outside this tool.

The music generation family is outside this tool.

The music transcription family is outside this tool.

## Limitations

Matching is static and exact; dead code counts, unsupported aliases are missed, and every route must occur in one module. Denial recognition depends on the listed wording. Source in other languages and runtime-only routes are invisible.

```text
describe cron expression
```

The bare phrase above can be misleading. A manual runbook step may use this wording without implementing the operation. Review the result manually.

```text
cron expression description
```

The bare phrase above can be misleading. A roadmap may mention a future feature without implementing it. Review the result manually.

```text
cron expression describer
```

The bare phrase above can be misleading. A hosted page may provide the operation outside the audited code. Review the result manually.

```text
human readable cron expression
```

The bare phrase above can be misleading. An instruction to enter a readable schedule may use this wording without a capability. Review the result manually.

```text
explain cron expression
```

The bare phrase above can be misleading. A documentation page may explain syntax without providing a feature. Review the result manually.

```text
cron expression explanation
```

The bare phrase above can be misleading. A specification section may use this wording without supporting code. Review the result manually.

```text
describe cron schedule
```

The bare phrase above can be misleading. A manual runbook step may use this wording without code. Review the result manually.

```text
cron schedule description
```

The bare phrase above can be misleading. A document may merely state that jobs are scheduled. Review the result manually.

```text
describe cron string
```

The bare phrase above can be misleading. A log may describe the string without producing a sentence about it. Review the result manually.

```text
cron string description
```

The bare phrase above can be misleading. A form field label may use this wording without a capability. Review the result manually.

```text
cron expression to text
```

The bare phrase above can be misleading. Serialization to a file may use this wording without explaining the schedule. Review the result manually.

```text
cron expression to words
```

The bare phrase above can be misleading. Speech synthesis may use this wording without explaining the schedule. Review the result manually.

```text
cron expression to sentence
```

The bare phrase above can be misleading. A template may insert a raw schedule into a sentence without explaining it. Review the result manually.

```text
cron expression in words
```

The bare phrase above can be misleading. A theoretical discussion may use this wording without supporting code. Review the result manually.

```text
cron expression in plain language
```

The bare phrase above can be misleading. A plain-language document about schedules may use this wording without a feature. Review the result manually.

```text
cron expression natural language description
```

The bare phrase above can be misleading. A chat feature may discuss schedules without producing the sentence. Review the result manually.

```text
describe cron value
```

The bare phrase above can be misleading. A document may describe the existence of a configuration value only. Review the result manually.

```text
cron value description
```

The bare phrase above can be misleading. A configuration field label may use this wording without a capability. Review the result manually.

```text
cron description
```

The bare phrase above can be misleading. A document may describe the scheduling service itself. Review the result manually.

```text
describe cron
```

The bare phrase above can be misleading. A document may describe the scheduling system itself. Review the result manually.

```text
convert cron expression to text
```

The bare phrase above can be misleading. Serialization to a file may use this wording without explaining the schedule. Review the result manually.

```text
cron expression description
```

The bare phrase above can be misleading. An external scheduler may produce the sentence instead of the audited code. Review the result manually.

```text
describe cron tab
```

The bare phrase above can be misleading. A whole tab is a file of jobs; this wording is outside the matching list. Review the result manually.

A descriptor constructor alone produces no sentence.

An options constructor alone produces no sentence.

A partial getter call describes one part, not the whole expression.

A translate call translates an already-produced sentence and does not produce one.

A str or repr call on a croniter object, a cronex expression, or a crontab job renders an object repr, the expression itself, or the cron line, never a sentence.

A formatted string rendering of a descriptor is not tracked.

A method attribute read is not a call.

A croniter construction or validity call judges the string and does not produce a sentence.

A CronValidator parse call parses the expression and does not produce a sentence.

A cronex CronExpression construction parses the expression, and its string form renders the expression itself, not a sentence.

A crontab CronTab construction is not evidence: a whole crontab is a file of jobs with commands, and CronTab has no description method at all.

A pattern match on a cron pattern alone is not evidence: a regex is not a description call.

A description call on a base that is not a descriptor instance or a descriptor class base is missed.

A bare import of a library with no call is not evidence, even when the import is the only thing the module does.

A doc that claims the checked capability in a roadmap, changelog, or TODO is still a claim: the tool reads prose, not intent.

A doc that denies the checked capability with a phrase outside the denial list is not recognised as a denial, and the claim side still fires if a claim phrase is present.

A claim in a file that is not the root README and has no docs path component is not read at all.

Evidence split across two modules is not evidence: each route must sit in a single module.

A route call on a name the module locally defines is shadowed and does not count, even when the local definition is a thin wrapper around the real library call.

Dead code counts: a description route in a function that is never called is still evidence, because the tool reads code, not execution.

A subprocess call that shells out to an external tool is not evidence by design: a shell command name in a string literal is never evidence.

A single generic input check with no cron leg is not evidence, even when the checked input happens to be a cron-expression string: checking that input exists says nothing about turning it into a sentence, and this family covers turning a cron-expression string into a human-readable sentence only.

A single email validation call with no cron leg is not evidence, even when the validated address sits next to a cron-expression field: email addresses are a different capability, and this family covers turning a cron-expression string into a human-readable sentence only.

A single phone number validation call with no cron leg is not evidence, even when the validated number sits next to a cron-expression field: phone numbers are a different capability, and this family covers turning a cron-expression string into a human-readable sentence only.

A single URL validation call with no cron leg is not evidence, even when the validated address contains a cron-expression string: web addresses are a different capability, and this family covers turning a cron-expression string into a human-readable sentence only.

A single IP address validation call with no cron leg is not evidence, even when the validated address sits next to a cron-expression field: numeric addresses are a different capability, and this family covers turning a cron-expression string into a human-readable sentence only.

A single domain validation call with no cron leg is not evidence, even when the validated name sits next to a cron-expression field: host names are a different capability, and this family covers turning a cron-expression string into a human-readable sentence only.

A single ISBN validation call with no cron leg is not evidence, even when the validated number sits next to a cron-expression field: book numbers are a different capability, and this family covers turning a cron-expression string into a human-readable sentence only.

A single ISSN validation call with no cron leg is not evidence, even when the validated number sits next to a cron-expression field: serial numbers are a different capability, and this family covers turning a cron-expression string into a human-readable sentence only.

A single IBAN validation call with no cron leg is not evidence, even when the validated number sits next to a cron-expression field: bank account numbers are a different capability, and this family covers turning a cron-expression string into a human-readable sentence only.

A single UUID validation call with no cron leg is not evidence, even when the validated identifier sits next to a cron-expression field: identifiers are a different capability, and this family covers turning a cron-expression string into a human-readable sentence only.

A single semver validation call with no cron leg is not evidence, even when the validated version sits next to a cron-expression field: version strings are a different capability, and this family covers turning a cron-expression string into a human-readable sentence only.

A single MAC address validation call with no cron leg is not evidence, even when the validated address sits next to a cron-expression field: hardware addresses are a different capability, and this family covers turning a cron-expression string into a human-readable sentence only.

A single extraction call with no cron leg is not evidence, even when the extracted data is a cron-expression string: reading data out of a document is a different capability, and this family covers turning a cron-expression string into a human-readable sentence only.

A generic name that a module locally defines is shadowed and does not count, even when the local definition turns schedule strings into sentences.

A generic name called through an alias chain the tracer cannot follow is missed.

The tool matches exact phrases only, not meaning: a doc that paraphrases the capability without using any listed phrase is invisible to the claim side, and a doc that uses a listed phrase for a different capability is flagged anyway.

The tool reads Python source only: a description implementation in another language in the same repo is invisible to the evidence side.

The tool never executes code and never touches the network: a description route that only exists at runtime is invisible.

The following claims are NOT in the phrase lists: generic input validation claims, JSON field-name claims, email sending claims, SMS sending claims, phone number validation claims, email validation claims, password strength claims, authentication claims, JSON extraction claims, barcode scanning claims, QR code scanning claims, audio mixing claims, audio generation claims, audio editing claims, source separation claims, speech recognition claims, text-to-speech claims, noise suppression claims, music generation claims, music transcription claims, video editing claims, screen recording claims, video generation claims, QR code generation claims, barcode generation claims, spreadsheet reading claims, spreadsheet generation claims, word-document reading claims, word-document generation claims, presentation reading claims, presentation generation claims, PDF extraction claims, PDF generation claims, PDF merging claims, PDF splitting claims, PDF encryption claims, PDF rotation claims, PDF form-filling claims, PDF redaction claims, PDF compression claims, PDF annotation claims, table extraction claims, OCR claims, document extraction claims, e-signature claims, payment-processing claims, URL validation claims, IP address validation claims, date validation claims, credit card validation claims, domain validation claims, ISBN validation claims, ISSN validation claims, IBAN validation claims, UUID validation claims, semver validation claims, MAC address validation claims, scheduled execution claims, timeout claims, and cron-expression validation claims. This family covers turning a cron-expression string into a human-readable sentence only.
