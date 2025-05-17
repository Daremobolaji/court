import streamlit as st

if 'auth' not in st.session_state or not st.session_state['auth']:
    st.warning("Please login from the main page.")
    st.stop()

st.title("📋 Court Dashboard")
st.write(f"Welcome, **{st.session_state['username']}**")

st.markdown("### Navigate:")
st.page_link("pages/2_Case_Filing.py", label="📄 File a Case")
st.page_link("pages/3_Case_Tracking.py", label="🔍 Track Your Case")
st.page_link("pages/4_Judge_Panel.py", label="⚖️ Judge/Admin Panel")
