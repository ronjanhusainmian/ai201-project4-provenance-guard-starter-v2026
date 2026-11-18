# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

A creator submits text and their creator ID through the /submit endpoint. The service validates the input and analyzes the text using an AI detection model and a writing-style analyzer. It combines both scores to determine a final classification and confidence level, records the results in a log, and returns the label to the reader. Creators can also appeal a classification they believe is incorrect.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
The model analyzes the text using a pretrained AI detection model and produces a score indicating how likely it is to be AI-generated.

**Why that might differ between human and AI writing:**
AI-generated text may contain patterns in word choice, sentence structure, and phrasing that differ from human writing. The model learns to recognize these patterns from its training data.

**What it can't see:**
The model cannot verify who actually wrote the text or whether AI was used. It may incorrectly flag human writing as AI-generated or fail to detect AI-generated text that has been edited.

### Signal two — the style signal

**What it measures:**
The style signal analyzes measurable writing features such as sentence length, vocabulary diversity, and punctuation patterns.

**Why that might differ between human and AI writing:**
AI-generated writing may have more consistent sentence structures and word choices, while human writing may show greater variation in style.

**What it can't see:**
Writing style alone cannot determine whether a person or AI wrote the text. Human writers may naturally use consistent writing patterns, while AI-generated text can be modified to appear more varied.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->
**The rule:**
The system combines the model and style scores using a weighted average. When the two signals disagree significantly (difference greater than 0.4), the system uses the lower score to reduce the risk of falsely labeling human writing as AI-generated.

**The numbers:**
- Model signal weight: 0.6 (60%)
- Style signal weight: 0.4 (40%)
- Disagreement threshold: 0.4
- Combined score ranges from 0 to 1, with higher scores indicating a greater likelihood of AI-generated writing.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
In my AI-generated test, the model signal scored 0.7079 while the style signal scored 0.4109. The signals disagreed about how likely the text was to be AI-generated. Since their difference was below 0.4, my rule used the weighted average and produced a combined score of 0.5891. This shows that the two signals can give different results for the same text. I also found that plain human writing received a combined score of 0.8065, which highlights the risk of false positives.


---

## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00–0.35 | This text appears more likely to have been written by a person. |
| unsure | Above 0.35, below 0.65 | We cannot reliably determine whether this text was written by a person or AI. |
| high-confidence AI | 0.65-1.00 | This text shows patterns associated with AI-generated writing, but this result is not definitive. |

**Why I worded the "unsure" one this way:**

I wanted the label to clearly communicate uncertainty without accusing the writer of using AI. Since neither signal can reliably prove authorship, the system should avoid making definitive claims.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Artificial intelligence is transforming the way people work and communicate. Many organizations are adopting AI systems to improve productivity and automate repetitive tasks. These technologies are becoming increasingly common across different industries.", "creator_id": "student1"}'
```

```json
{
  "confidence": 0.8288,
  "content_id": "177fba70-85eb-4bb7-8552-610911ff1123",
  "guess": "ai",
  "label": "Pending final scoring",
  "model_score": 0.8288,
  "style_score": null
}
```

**An appeal**

I tested the appeal endpoint using a real `content_id` from an earlier submission.

**Request:**
```bash
curl -X POST http://127.0.0.1:5000/appeal \
-H "Content-Type: application/json" \
-d '{"content_id": "c49e0033-fd23-47a2-9abe-5e2bf1afa0b3", "reasoning": "I wrote this text myself and believe the classification is incorrect."}'
```

**Response:**
```json
{
  "content_id": "c49e0033-fd23-47a2-9abe-5e2bf1afa0b3",
  "message": "Your appeal has been recorded and is under review.",
  "status": "under_review"
}
```

**Appeal entry:**
```json
{
  "content_id": "c49e0033-fd23-47a2-9abe-5e2bf1afa0b3",
  "creator_id": "student1",
  "event": "appeal",
  "reasoning": "I wrote this text myself and believe the classification is incorrect.",
  "status": "under_review"
}
```

**Result:** The appeal endpoint successfully recorded the appeal and set its status to under_review. The original decision remained unchanged, and both entries appeared in the audit log.


**What the log shows afterwards**

I checked the audit log using:
```bash
curl "http://127.0.0.1:5000/log?limit=2"
```


**Response:**
```json
{
  "content_id": "c49e0033-fd23-47a2-9abe-5e2bf1afa0b3",
  "creator_id": "student1",
  "guess": "ai",
  "model_score": 0.8444,
  "style_score": 0.6392,
  "combined_score": 0.7623,
  "status": "decided"
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I used AI to help me understand the purpose of the different Python files, how their functions work, and how they interact with each other.
- *What came back:* AI explained the code structure, the role of each function, and how data flows through the detection and scoring process.
- *What I changed:* I used these explanations to better understand the existing code and identify where I needed to make changes.

**Moment 2**

- *What I asked for:* I asked AI for help with Python syntax, Flask endpoints, function calls, and formatting JSON responses.
- *What came back:* AI provided syntax examples and explained how to use the relevant functions and libraries.
- *What I changed:* I adapted the examples to my project, tested the code using terminal commands, and made adjustments based on the results.

**Moment 3**

- *What I asked for:* I asked AI for help writing and debugging the Python scripts used to run the evaluation and appeal tests in Unit 8.
- *What came back:* AI provided code examples and helped identify issues with how the scripts handled API responses and content IDs.
- *What I changed:* I updated the scripts to use the correct content IDs returned by the API, ran the tests in the terminal, and checked that the results matched the expected behavior.
<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
I chose 10 requests per minute because a normal user would only submit a few pieces of writing at a time. This limit allows regular users to use the service while preventing scripts from sending too many requests quickly. The 200 requests per day limit also helps prevent repeated attempts to test and bypass the detector.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
<!-- differently — one script can look like a thousand callers, and one household
can look like one. -->
A caller is identified by their IP address. This means multiple users sharing the same IP address may share a rate limit, while someone using different IP addresses could bypass it.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->


| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `0610eabb-7a42-4ece-ba70-a9a5c6658c74` | human | 0.164 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `3ae20c73-9355-4c67-957d-b0074d319e7d` | unsure | 0.498 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `9eae34a6-a206-43fd-928d-cf1528834de6` | unsure | 0.593 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `f482a49b-43ec-4171-9ff4-3327de314fbf` | unsure | 0.601 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `8c0d7bb6-2975-47bb-8157-54bf595c2282` | human | 0.337 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `013f5a78-d5a4-448e-9fb1-d0614425b34a` | unsure | 0.498 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `00efa5d5-a66d-4a83-bf66-fa7623bda1ed` | unsure | 0.570 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `4874e4e2-cf50-4eb1-9b1b-5d590b872392` | unsure | 0.367 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `0200499f-d3d5-40d7-9098-f9988db5c347` | unsure | 0.612 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `45525d47-303b-4b7f-a1e6-461fc93f4041` | ai | 0.879 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `222c7f45-ed36-4baf-8e15-724020f1e8fa` | unsure | 0.590 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `c7ecd63b-c9f1-4907-86d1-fabfc59363b2` | ai | 0.703 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `13997208-77ab-4000-9aa4-eebb67488473` | ai | 0.732 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `611261c6-ecdd-4e15-adae-35aa188f7e8a` | ai | 0.725 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `e5cfd398-d07f-4176-acac-ab90e71732f0` | ai | 0.743 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `d686b6df-0986-4c9c-ae22-24127ea03484` | ai | 0.737 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c863a2cf-5666-4226-b103-24caffbaae2c` | ai | 0.730 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `57ccf2a0-2067-4275-840e-a60e8cfa2479` | unsure | 0.388 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `5fb4fa47-8d56-4d50-8878-1963d31805c8` | unsure | 0.443 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `ef08c798-c957-4c88-b7ad-37e8bd23d6a3` | human | 0.270 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `1ce7f71a-28ff-4116-8fcd-05200f50184d` | unsure | 0.571 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `a4456b93-93ac-4b8f-bed9-a13791a2946c` | unsure | 0.499 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `5f9f61a0-ffd2-4a37-8750-6fc5f4383bca` | unsure | 0.501 | HELD |


**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-15T22:48:35+00:00", "content_id": "fbd611e1-f0b5-4857-89d2-0145c385dcf3", "creator_id": "attacker_flood", "guess": "human", "model_score": 0.0287, "style_score": 0.6667, "combined_score": 0.0287, "label": "This text appears more likely to have been written by a person.", "status": "decided"},
{"timestamp": "2026-11-15T22:48:35+00:00", "content_id": "12eca590-252a-4fb0-a87d-ba870380979c", "creator_id": "attacker_flood", "guess": "human", "model_score": 0.0287, "style_score": 0.6667, "combined_score": 0.0287, "label": "This text appears more likely to have been written by a person.", "status": "decided"},
{"timestamp": "2026-11-15T22:48:35+00:00", "content_id": "8d21bf09-7a8f-456e-9c99-ba97197bf9c0", "creator_id": "attacker_flood", "guess": "human", "model_score": 0.0287, "style_score": 0.6667, "combined_score": 0.0287, "label": "This text appears more likely to have been written by a person.", "status": "decided"},
{"timestamp": "2026-11-15T22:48:35+00:00", "content_id": "4187adeb-7781-4d1a-9364-7ea493ace980", "creator_id": "attacker_flood", "guess": "human", "model_score": 0.0287, "style_score": 0.6667, "combined_score": 0.0287, "label": "This text appears more likely to have been written by a person.", "status": "decided"},
{"timestamp": "2026-11-15T22:48:35+00:00", "content_id": "d5d0d5f5-c855-4c62-a418-cb26f52bc28f", "creator_id": "attacker_flood", "guess": "human", "model_score": 0.0287, "style_score": 0.6667, "combined_score": 0.0287, "label": "This text appears more likely to have been written by a person.", "status": "decided"},
{"timestamp": "2026-11-15T22:48:35+00:00", "content_id": "549c70e5-13d0-43ff-883d-e8a24586a5b4", "creator_id": "attacker_flood", "guess": "human", "model_score": 0.0287, "style_score": 0.6667, "combined_score": 0.0287, "label": "This text appears more likely to have been written by a person.", "status": "decided"},
{"timestamp": "2026-11-15T22:48:35+00:00", "content_id": "d974eb63-daae-4e2a-acfe-ac3c471cbc9e", "creator_id": "attacker_flood", "guess": "human", "model_score": 0.0287, "style_score": 0.6667, "combined_score": 0.0287, "label": "This text appears more likely to have been written by a person.", "status": "decided"},
{"timestamp": "2026-11-15T22:48:35+00:00", "content_id": "bb54385e-0ea6-43fb-a5df-58e1ee825790", "creator_id": "attacker_flood", "guess": "human", "model_score": 0.0287, "style_score": 0.6667, "combined_score": 0.0287, "label": "This text appears more likely to have been written by a person.", "status": "decided"},
{"timestamp": "2026-11-15T22:48:35+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "10 per 1 minute"},
{"timestamp": "2026-11-15T22:48:35+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "10 per 1 minute"}


```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

The worst outcome was FP03, where writing from a non-native English speaker was classified as AI-generated with a score of 0.732. This is concerning because the system could incorrectly accuse someone of using AI simply because of their writing style. It shows that the detector can produce false positives and should not be used as definitive proof of AI-generated writing.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False Positives | No more than 1/10 human samples labeled AI | 7/10 AI | 7/10 AI | 7/10 AI | MISSED |
| 2. Score Spread | AI average score at least 0.15 higher than human average | -0.0869 | -0.0869 | -0.0869 | MISSED |
| 3. Label Coverage | All 3 labels appear across 10 samples | 2/3 labels | 2/3 labels | 2/3 labels | MISSED |
| 4. Appeal Path | All 3 appeals successfully update status and appear in log | 3/3 | 3/3 | 3/3 | MET |
| 5. Bad Input Handling | All 3 invalid inputs return errors without crashing | 3/3 HTTP 400 | 3/3 HTTP 400 | 3/3 HTTP 400 | MET |

**Real output from one trial**

Source: `results/run_2026-11-15_1951_before.md`, generated by `run_eval.py` using the `run_eval.py --label before` command.

Example from Criterion 1 (False Positives), Trial 1:

```json
{
  "status": 200,
  "guess": "ai",
  "confidence": 0.6649,
  "model_score": 0.6685,
  "style_score": 0.6596,
  "label": "This text shows patterns associated with AI-generated writing, but this result is not definitive.",
  "sent": "Our group met in the library to work on our project. We divided the re"
}
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

**1. False Positives — MISSED**
- **Stage:** Signal scoring and label mapping.
- **Mechanism:** 7 out of 10 human-written samples were classified as AI. The detector assigned high AI scores to human writing, causing incorrect labels.

**2. Score Spread — MISSED**
- **Stage:** Signal scoring and combining rule.
- **Mechanism:** Human-written samples had a higher average score (0.6470) than AI-generated samples (0.5601). The signals did not distinguish the two groups correctly, resulting in poor score separation.

**3. Label Coverage — MISSED**
- **Stage:** Label mapping.
- **Mechanism:** Only `ai` and `unsure` labels appeared. None of the samples received a `human` label because their combined scores did not fall below the required threshold.

**Overall Pattern**

All three misses appear related to the detection and scoring system. Human-written text frequently received high AI scores, affecting false positives, score separation, and label coverage. The appeal process and input validation worked correctly, so the main issue appears to be with classification rather than the API routes.


---

## The Improvement

**What I changed:**
I increased `AI_THRESHOLD` by 0.10 in `config.py`. This means the detector now requires a higher score before labeling text as AI.

**Which diagnosis pointed at it:**
The false positive test showed that 7 out of 10 human-written samples were incorrectly labeled as AI. I increased the threshold to reduce these incorrect classifications.


### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

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



**Did it help, and how do I know:**

Yes, the change reduced false positives from 7/10 to 0/10 across all three trials. However, it also reduced label coverage from 2/3 to 1/3 because all samples in that test received the `unsure` label. The score spread remained unchanged at -0.0869. This shows that the change reduced incorrect AI labels but did not improve the detector's ability to distinguish AI-generated text from human writing.

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

| Criterion | Before | After | Verdict (After) |
|---|---|---|---|
| 1. False Positives | 7/10 labeled AI | 0/10 labeled AI | MET |
| 2. Score Spread | -0.0869 | -0.0869 | MISSED |
| 3. Label Coverage | 2/3 labels | 1/3 labels | MISSED |
| 4. Appeal Path | 3/3 successful appeals | 3/3 successful appeals | MET |
| 5. Bad Input Handling | 3/3 HTTP 400 | 3/3 HTTP 400 | MET |



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->
**Score Spread:** The detector still assigns higher average scores to human-written text than AI-generated text. I would improve the model and stylometry signals to better distinguish the two groups.

**Label Coverage:** The detector now produces too many `unsure` labels. I would adjust both the AI and human thresholds using more test samples to find a better balance.

**Attack Handling:** I would review any attacks that still succeed after the change and identify which signals they exploit.

**Why I stopped:** I made one targeted change and evaluated its impact. Further improvements would require more testing and adjustments to the scoring system.



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

I would prioritize reducing false accusations against human writers, even if that means more AI-generated text goes undetected. Human writers would otherwise face unfair accusations, while the cost of this choice would fall on people relying on the detector to identify AI-generated content.

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**




## Capstone

### The System
I am extending my Provenance Guard web service from Units 7–8. The system analyzes submitted text using GPT-2 perplexity and stylometry, combines the scores, and classifies the text as AI, human, or unsure.

### The Shape
**Shape A — Deploy and Instrument**

I will make the existing Flask service reproducible locally, add structured logging for each request, and measure how long each request takes.

### What's New
- A `RUNNING.md` file with instructions to start the service.
- Structured logs containing timestamps, request information, results, and execution time.
- Measurements of how long text classification takes.

### What's Out of Scope
- Training or replacing the detection models.
- Changing the classification thresholds or scoring logic.
- Adding new API endpoints or detection features.


### Unit 9 - Extension Testing

- Normal submission: HTTP 200, with detection scores returned.
- Simulated timeout: HTTP 504, with a clear error message.
- Existing system tests: Passed after adding timeout handling.

