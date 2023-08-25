import streamlit as st


def setup_page(page_title):
    st.set_page_config(
        page_title=page_title,
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title(page_title)
    return st
