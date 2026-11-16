"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""


SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "I spent most of yesterday studying for my algorithms exam. I understood the lectures, but some of the homework problems were still confusing. I went through the solutions again and tried solving them without looking at my notes.",
            "Our group met in the library to work on our project. We divided the remaining tasks and discussed how to test the application. I worked on fixing a few bugs and helped another team member understand the code.",
            "Last weekend I went grocery shopping and cooked dinner with my friends. We tried making something new, but it took much longer than expected. The food turned out pretty good in the end.",
            "I was having trouble understanding a concept in class, so I went to office hours. The professor explained it using a smaller example, which made the problem easier to understand.",
            "I started working on my assignment early because I knew I would be busy later in the week. I finished most of it on Monday and used the remaining time to check my answers.",
            "My laptop stopped connecting to the internet during a meeting. I restarted it twice before realizing that the problem was with the network. After reconnecting, everything worked normally.",
            "I enjoy working on programming projects because I can see the results of what I build. Sometimes debugging takes longer than writing the code, but figuring out the problem is satisfying.",
            "We had a team meeting to discuss our progress. Everyone shared what they had completed and what they were struggling with. We decided to focus on the most important tasks first.",
            "I missed the bus this morning and had to walk to campus. It was colder than I expected, so I stopped to get coffee before going to class.",
            "I spent the afternoon reviewing my notes and practicing problems. Some questions were straightforward, while others required several attempts before I understood the solution.",
        ],
    },
    {
        "name": "score spread",
        "criterion": 2,
        "texts": [
            "Artificial intelligence is transforming modern industries by automating repetitive tasks, improving operational efficiency, and enabling organizations to make data-driven decisions.",
            "Machine learning algorithms identify patterns in large datasets and use these patterns to make predictions. Their effectiveness depends on data quality, model selection, and evaluation.",
            "Cloud computing provides scalable computing resources over the internet. Organizations can adjust infrastructure capacity based on demand while reducing the need for physical hardware.",
            "Effective communication is essential for successful teamwork. Clear expectations, regular feedback, and shared responsibilities help teams coordinate their efforts and achieve common goals.",
            "Cybersecurity involves protecting computer systems, networks, and sensitive information from unauthorized access. Strong authentication, regular updates, and monitoring help reduce security risks.",
            "I spent most of yesterday studying for my algorithms exam. I understood the lectures, but some of the homework problems were still confusing. I went through the solutions again and tried solving them without looking at my notes.",
            "Our group met in the library to work on our project. We divided the remaining tasks and discussed how to test the application. I worked on fixing a few bugs and helped another team member understand the code.",
            "Last weekend I went grocery shopping and cooked dinner with my friends. We tried making something new, but it took much longer than expected. The food turned out pretty good in the end.",
            "I was having trouble understanding a concept in class, so I went to office hours. The professor explained it using a smaller example, which made the problem easier to understand.",
            "I started working on my assignment early because I knew I would be busy later in the week. I finished most of it on Monday and used the remaining time to check my answers.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "Artificial intelligence is transforming modern industries by automating repetitive tasks, improving operational efficiency, and enabling organizations to make data-driven decisions.",
            "Machine learning algorithms identify patterns in large datasets and use these patterns to make predictions. Their effectiveness depends on data quality, model selection, and evaluation.",
            "Cloud computing provides scalable computing resources over the internet. Organizations can adjust infrastructure capacity based on demand while reducing the need for physical hardware.",
            "Effective communication is essential for successful teamwork. Clear expectations, regular feedback, and shared responsibilities help teams coordinate their efforts and achieve common goals.",
            "Cybersecurity involves protecting computer systems, networks, and sensitive information from unauthorized access. Strong authentication, regular updates, and monitoring help reduce security risks.",
            "I spent most of yesterday studying for my algorithms exam. I understood the lectures, but some of the homework problems were still confusing. I went through the solutions again and tried solving them without looking at my notes.",
            "Our group met in the library to work on our project. We divided the remaining tasks and discussed how to test the application. I worked on fixing a few bugs and helped another team member understand the code.",
            "Last weekend I went grocery shopping and cooked dinner with my friends. We tried making something new, but it took much longer than expected. The food turned out pretty good in the end.",
            "I was having trouble understanding a concept in class, so I went to office hours. The professor explained it using a smaller example, which made the problem easier to understand.",
            "I started working on my assignment early because I knew I would be busy later in the week. I finished most of it on Monday and used the remaining time to check my answers.",
        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        "texts": [
            "I worked on my programming assignment yesterday and tested the code before submitting it.",
            "Our team met to discuss the project requirements and divide the remaining tasks.",
            "I reviewed my class notes and practiced several problems before the exam.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_missing_text"},
            {"text": "", "creator_id": "eval_empty_text"},
            {"text": "Testing missing creator ID"},
        ],
    },
]



def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
