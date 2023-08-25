import pandas as pd
import streamlit as st


@st.cache_data
def load_data(file: str, **kwargs) -> pd.DataFrame:
    data = pd.read_csv(file, **kwargs)
    return data
