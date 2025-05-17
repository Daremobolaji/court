import streamlit as st
import uuid
from utils.db_utils import save_case

st.title("📄 File a New Case")

if 'auth' not in st.session_state or not st.session_state['auth']:
    st.warning("Please login first.")
    st.stop()

case_title = st.text_input("Case Title")
description = st.text_area("Case Description")
submit = st.button("Submit Case")

if submit:
    case_id = str(uuid.uuid4())
    case_data = {
        "id": case_id,
        "user": st.session_state['username'],
        "title": case_title,
        "description": description,
        "status": "Filed"
    }
    save_case(case_data)
    st.success(f"Case submitted successfully! Case ID: {case_id}")
