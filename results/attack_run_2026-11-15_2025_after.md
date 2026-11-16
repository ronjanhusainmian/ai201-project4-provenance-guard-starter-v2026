# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-15 20:25
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.


| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `14db34ab-ad60-4e51-bcb1-8c92f4647922` | human | 0.164 | GOT THROUGH |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `99b3426d-7c45-4593-81dc-f5ef5003446c` | unsure | 0.498 | GOT THROUGH |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `9a0c4d07-fa13-4af3-9945-043f8f18b5d9` | unsure | 0.593 | GOT THROUGH |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `5ffb6bb5-722f-4ba9-85b3-c612ff709830` | unsure | 0.601 | GOT THROUGH |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `9814bce7-4821-427e-8018-4ae0afc4fd10` | human | 0.337 | GOT THROUGH |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `9c9c78c6-699b-4d06-af3b-d64d6f0c644a` | unsure | 0.498 | GOT THROUGH |
| EV07 | evasion | signal two: padding with punctuation | 200 | `b3d8354a-d487-4662-a7ed-421e779ec599` | unsure | 0.570 | GOT THROUGH |
| EV08 | evasion | signal one: text below the token window | 200 | `396658cc-fa03-45f1-97ef-540404b61d4b` | unsure | 0.367 | GOT THROUGH |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `ab5d65e1-c8b1-43b8-ae37-54a72de68e13` | unsure | 0.612 | GOT THROUGH |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `6d672b5a-f7ac-4c52-880a-c3203e626fb6` | ai | 0.879 | BLOCKED |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c9265516-1a4e-423a-afb6-c7684b88fb39` | unsure | 0.590 | NO FALSE POSITIVE |
| FP02 | false_positive | human writing in a formal register | 200 | `17eb2191-5daa-4336-8f46-b768f79fd7fd` | unsure | 0.703 | NO FALSE POSITIVE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `3fd9d2cc-b057-4b70-aa15-b4e39c69f2d5` | unsure | 0.732 | NO FALSE POSITIVE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `19237c90-4e87-4170-bad5-010dc9f67ead` | unsure | 0.725 | NO FALSE POSITIVE |
| FP05 | false_positive | technical documentation written by a person | 200 | `79380bcd-486e-4076-b47e-91b1705ea3de` | unsure | 0.743 | NO FALSE POSITIVE |
| FP06 | false_positive | a person imitating a formal template | 200 | `ff52d105-6ea6-4cf8-be22-3db573f8311b` | unsure | 0.737 | NO FALSE POSITIVE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `0719ce7a-23c0-421a-b625-21bec0e04672` | unsure | 0.730 | NO FALSE POSITIVE |
| FP08 | false_positive | very short genuine human submission | 200 | `1676229a-b276-4e8f-8d99-988ecc18eedf` | unsure | 0.388 | NO FALSE POSITIVE |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `b575a313-e7cb-4018-95b2-a76ac2653a4d` | unsure | 0.443 | NOT VERIFIED |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `947ab7af-6915-41f3-8c4f-c4f6d552ed18` | human | 0.270 | NOT VERIFIED |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `125d2061-728e-441b-ad6b-0c9d763d4971` | unsure | 0.571 | NOT VERIFIED |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `be4f391a-a27e-4be8-8ded-aaade191e0a0` | unsure | 0.499 | BLOCKED |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `2c92cc1b-b33c-4c22-8c7c-c134f89bcde2` | unsure | 0.501 | NOT VERIFIED |

| PI06 | prompt_injection | instruction plus real human text | 200 | `b3b07008-a1f4-4e05-9603-376dad7a532c` | unsure | 0.557 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `107c6b68-f520-474b-9e3b-6d6d9947d024` | human | 0.000 |  |
| MF04 | malformed | text is only punctuation | 200 | `3d35dba9-407d-46ec-8496-300bf48c00d1` | human | 0.011 |  |
| MF05 | malformed | text is a very long single word | 200 | `74c6599b-4a2c-4289-a4ff-4ee45ba72568` | ai | 0.865 |  |
| MF06 | malformed | text is emoji only | 200 | `7e384a0e-1c4d-4f84-86fb-e23d2604de82` | ai | 0.998 |  |
| MF07 | malformed | text is right-to-left script | 200 | `19b76276-5ddd-4b63-89d0-43974ba23280` | ai | 0.944 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `3d4eedce-a679-4383-b5cc-4f716392f2ce` | ai | 0.910 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bc4a8776-c820-4374-8954-3199ebaa4168` | human | 0.029 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b78adaaf-4fa0-4791-bd4e-ed059e50b70e` | human | 0.029 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `71a868e5-5dbf-4dee-aa1b-994d800520e9` | human | 0.029 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e4896bdc-3cff-40d0-8411-8642d70aa3e1` | human | 0.029 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dbc7efe7-1f59-4f3f-a713-177f20331cfa` | human | 0.029 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8cf6e118-cff6-4dca-b8d2-ab7e8312aba2` | human | 0.029 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d3c2b229-7a98-4951-b733-d7b1e44b5129` | human | 0.029 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `670e2b60-82b2-489b-ba94-c3ce133581c4` | human | 0.029 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2f5796dd-82ad-45be-9446-031b3f6554df` | human | 0.029 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0c249b13-6844-4ff6-bdcd-1faf44e71e37` | human | 0.029 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 200 | `39a90fcb-0b74-4bb3-bd27-dcd9b4e91fc8` | human | 0.029 |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 200 | `26d31d1c-ad2e-47c4-ace9-2a0c02f13a61` | human | 0.029 |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "14db34ab-ad60-4e51-bcb1-8c92f4647922",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.1635,
  "model_score": 0.1635,
  "style_score": 0.6022,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "99b3426d-7c45-4593-81dc-f5ef5003446c",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4984,
  "model_score": 0.5943,
  "style_score": 0.3546,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "9a0c4d07-fa13-4af3-9945-043f8f18b5d9",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5934,
  "model_score": 0.6662,
  "style_score": 0.4841,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "5ffb6bb5-722f-4ba9-85b3-c612ff709830",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6013,
  "model_score": 0.6114,
  "style_score": 0.5861,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "9814bce7-4821-427e-8018-4ae0afc4fd10",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3372,
  "model_score": 0.3212,
  "style_score": 0.3612,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "9c9c78c6-699b-4d06-af3b-d64d6f0c644a",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4977,
  "model_score": 0.5727,
  "style_score": 0.3853,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "b3d8354a-d487-4662-a7ed-421e779ec599",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5702,
  "model_score": 0.5862,
  "style_score": 0.5463,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "396658cc-fa03-45f1-97ef-540404b61d4b",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3666,
  "model_score": 0.2452,
  "style_score": 0.5488,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "ab5d65e1-c8b1-43b8-ae37-54a72de68e13",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6117,
  "model_score": 0.7042,
  "style_score": 0.4729,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "6d672b5a-f7ac-4c52-880a-c3203e626fb6",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8791,
  "model_score": 0.9792,
  "style_score": 0.729,
  "label": "This text shows patterns associated with AI-generated writing, but this result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "c9265516-1a4e-423a-afb6-c7684b88fb39",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5896,
  "model_score": 0.6175,
  "style_score": 0.5478,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "17eb2191-5daa-4336-8f46-b768f79fd7fd",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7028,
  "model_score": 0.7387,
  "style_score": 0.649,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "3fd9d2cc-b057-4b70-aa15-b4e39c69f2d5",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.732,
  "model_score": 0.8051,
  "style_score": 0.6223,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "19237c90-4e87-4170-bad5-010dc9f67ead",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7247,
  "model_score": 0.8329,
  "style_score": 0.5623,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "79380bcd-486e-4076-b47e-91b1705ea3de",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7425,
  "model_score": 0.8005,
  "style_score": 0.6554,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "ff52d105-6ea6-4cf8-be22-3db573f8311b",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.7369,
  "model_score": 0.8814,
  "style_score": 0.5202,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "0719ce7a-23c0-421a-b625-21bec0e04672",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7301,
  "model_score": 0.8816,
  "style_score": 0.5029,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "1676229a-b276-4e8f-8d99-988ecc18eedf",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3879,
  "model_score": 0.3223,
  "style_score": 0.4863,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "b575a313-e7cb-4018-95b2-a76ac2653a4d",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4426,
  "model_score": 0.4625,
  "style_score": 0.4128,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "947ab7af-6915-41f3-8c4f-c4f6d552ed18",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.27,
  "model_score": 0.2044,
  "style_score": 0.3685,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "125d2061-728e-441b-ad6b-0c9d763d4971",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.571,
  "model_score": 0.5943,
  "style_score": 0.536,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "be4f391a-a27e-4be8-8ded-aaade191e0a0",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4993,
  "model_score": 0.4998,
  "style_score": 0.4985,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "2c92cc1b-b33c-4c22-8c7c-c134f89bcde2",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5014,
  "model_score": 0.6401,
  "style_score": 0.2934,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "b3b07008-a1f4-4e05-9603-376dad7a532c",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5573,
  "model_score": 0.5583,
  "style_score": 0.5558,
  "label": "We cannot reliably determine whether this text was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "107c6b68-f520-474b-9e3b-6d6d9947d024",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.0,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "3d35dba9-407d-46ec-8496-300bf48c00d1",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.0112,
  "model_score": 0.0112,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "74c6599b-4a2c-4289-a4ff-4ee45ba72568",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8652,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "This text shows patterns associated with AI-generated writing, but this result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "7e384a0e-1c4d-4f84-86fb-e23d2604de82",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9981,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "This text shows patterns associated with AI-generated writing, but this result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "19b76276-5ddd-4b63-89d0-43974ba23280",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9438,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "This text shows patterns associated with AI-generated writing, but this result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "3d4eedce-a679-4383-b5cc-4f716392f2ce",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.9102,
  "model_score": 0.9876,
  "style_score": 0.7941,
  "label": "This text shows patterns associated with AI-generated writing, but this result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "bc4a8776-c820-4374-8954-3199ebaa4168",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "b78adaaf-4fa0-4791-bd4e-ed059e50b70e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "71a868e5-5dbf-4dee-aa1b-994d800520e9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "e4896bdc-3cff-40d0-8411-8642d70aa3e1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "dbc7efe7-1f59-4f3f-a713-177f20331cfa",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "8cf6e118-cff6-4dca-b8d2-ab7e8312aba2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "d3c2b229-7a98-4951-b733-d7b1e44b5129",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "670e2b60-82b2-489b-ba94-c3ce133581c4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "2f5796dd-82ad-45be-9446-031b3f6554df",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "0c249b13-6844-4ff6-bdcd-1faf44e71e37",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 200,
  "content_id": "39a90fcb-0b74-4bb3-bd27-dcd9b4e91fc8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 200,
  "content_id": "26d31d1c-ad2e-47c4-ace9-2a0c02f13a61",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "This text appears more likely to have been written by a person.",
  "error": null,
  "verdict": ""
}
```
