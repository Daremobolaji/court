import json
import os

DATA_PATH = "courtjudicial/data/users.json"

def load_users():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DATA_PATH, "w") as f:
        json.dump(users, f, indent=4)

def login_user(username, password):
    users = load_users()
    return username in users and users[username]["password"] == password

def signup_user(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = {"password": password, "role": "user"}
    save_users(users)
    return True

def is_logged_in():
    return "auth" in st.session_state and st.session_state['auth']

def logout_user():
    st.session_state.clear()
