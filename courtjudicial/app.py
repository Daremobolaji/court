import streamlit as st
from auth.auth_manager import login_user, signup_user, is_logged_in, logout_user

st.set_page_config(page_title="Court Judicial System", layout="centered")

if 'auth' not in st.session_state:
    st.session_state['auth'] = False

st.title("⚖️ Court Judicial Automated Process Flow System")

menu = st.sidebar.selectbox("Menu", ["Login", "Sign Up"] if not st.session_state['auth'] else ["Logout"])

if menu == "Login" and not st.session_state['auth']:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(username, password):
            st.success(f"Welcome {username}!")
            st.session_state['auth'] = True
            st.session_state['username'] = username
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error("Invalid credentials.Check again")

elif menu == "Sign Up" and not st.session_state['auth']:
    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")
    if st.button("Sign Up"):
        if signup_user(new_user, new_pass):
            st.success("Account created! Please login.")
        else:
            st.warning("Username already exists.")

elif menu == "Logout":
    logout_user()
    st.success("Logged out successfully.")
    st.session_state['auth'] = False
