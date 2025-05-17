import streamlit as st
from utils.db_utils import get_user_cases

st.title("🔍 Track Your Cases")

if 'auth' not in st.session_state or not st.session_state['auth']:
    st.warning("Please login first.")
    st.stop()

user_cases = get_user_cases(st.session_state['username'])

if not user_cases:
    st.info("No cases found.")
else:
    for case in user_cases:
        st.markdown(f"**ID:** {case['id']} | **Title:** {case['title']} | **Status:** {case['status']}")
