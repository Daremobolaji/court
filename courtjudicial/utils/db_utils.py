import json
import os
#dir=os.getcwd()
#root = dir.replace("\\", "/")+'/'
CASE_DB = "courtjudicial/data/case.json"


def load_cases():
    if not os.path.exists(CASE_DB):
        return []
    with open(CASE_DB, "r") as f:
        return json.load(f)

def save_cases(cases):
    with open(CASE_DB, "w") as f:
        json.dump(cases, f, indent=4)

def save_case(case):
    cases = load_cases()
    cases.append(case)
    save_cases(cases)

def get_user_cases(username):
    return [c for c in load_cases() if c['user'] == username]

def get_all_cases():
    return load_cases()

def update_case_status(case_id, new_status):
    cases = load_cases()
    for c in cases:
        if c['id'] == case_id:
            c['status'] = new_status
    save_cases(cases)
