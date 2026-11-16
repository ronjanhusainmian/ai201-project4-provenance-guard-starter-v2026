
import requests
import json
import uuid

BASE = "http://127.0.0.1:5000"

for trial in range(1, 4):
    passed = 0

    for i in range(1, 4):
        content_id = f"appeal_{uuid.uuid4().hex[:10]}"

        submit = requests.post(f"{BASE}/submit", json={
            "content_id": content_id,
            "creator_id": f"tester_{i}",
            "text": "I worked on my programming assignment yesterday."
        })

        content_id = submit.json()["content_id"]

        appeal = requests.post(f"{BASE}/appeal", json={
            "content_id": content_id,
            "reasoning": "I believe this classification is incorrect."
        })

        log = requests.get(f"{BASE}/log", params={
            "content_id": content_id
        })

        if (
            submit.status_code == 200
            and appeal.status_code == 200
            and appeal.json().get("status") == "under_review"
            and log.status_code == 200
            and "under_review" in log.text
            and content_id in log.text
        ):
            passed += 1
        else:
            print(f"  Test {i}: submit={submit.status_code}, appeal={appeal.status_code}, log={log.status_code}")

    print(f"Trial {trial}: {passed}/3 — {'MET' if passed == 3 else 'MISSED'}")
