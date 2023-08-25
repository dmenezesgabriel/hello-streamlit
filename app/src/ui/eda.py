import streamlit as st
from utils.data import load_data


def upload_sheet():
    with st.sidebar:
        st.header("Upload file")
        uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])

    if uploaded_file is None:
        st.info("Upload a file through the file uploader.")
        st.stop()
    return uploaded_file


def view_sheet(uploaded_file):
    df = load_data(uploaded_file)

    with st.expander("Data Preview"):
        st.dataframe(df)
