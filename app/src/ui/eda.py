import pandas as pd
import streamlit as st


def render_preview_ui(df: pd.DataFrame):
    with st.expander("Preview"):
        st.dataframe(df)


def upload_sheet():
    st.header("Upload file")
    uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])

    if uploaded_file is None:
        st.info("Upload a file through the file uploader.")
        st.stop()
    return uploaded_file
