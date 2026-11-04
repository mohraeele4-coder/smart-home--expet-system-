import streamlit as st

def t(en_text, ar_text):
    if st.session_state.get("language", "EN") == "AR":
        return ar_text
    return en_text