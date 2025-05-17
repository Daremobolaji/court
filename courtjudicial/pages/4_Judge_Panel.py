import streamlit as st
from utils.db_utils import get_all_cases, update_case_status

st.title("⚖️ Judge/Admin Panel")

if 'auth' not in st.session_state or not st.session_state['auth']:
    st.warning("Access restricted.")
    st.stop()

cases = get_all_cases()

for case in cases:
    st.subheader(f"{case['title']} (ID: {case['id']})")
    st.write(f"User: {case['user']}")
    st.write(f"Status: {case['status']}")
    new_status = st.selectbox("Update Status", ["Filed", "Under Review", "Closed"], key=case['id'])
    if st.button("Update", key=case['id'] + "_btn"):
        update_case_status(case['id'], new_status)
        st.success("Status updated.")
