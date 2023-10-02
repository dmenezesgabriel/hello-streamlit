from typing import Dict, Set

import pandas as pd
import plotly.express as px
import streamlit as st

from ui.cross_filter import render_plotly_ui, render_preview_ui

st.set_page_config(
    page_title="Cross Filter",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data
def load_data() -> pd.DataFrame:
    return px.data.tips()


def initialize_state():
    for q in ["bill_to_tip", "size_to_time", "day"]:
        if f"{q}_query" not in st.session_state:
            st.session_state[f"{q}_query"] = set()

    if "counter" not in st.session_state:
        st.session_state["counter"] = 0


def update_state(current_query: Dict[str, Set]):
    rerun = False
    for q in ["bill_to_tip", "size_to_time", "day"]:
        if current_query[f"{q}_query"] - st.session_state[f"{q}_query"]:
            st.session_state[f"{q}_query"] = current_query[f"{q}_query"]
            rerun = True
    if rerun:
        st.experimental_rerun()


def reset_state_callback():
    for q in ["bill_to_tip", "size_to_time", "day"]:
        st.session_state[f"{q}_query"] = set()

    st.session_state["counter"] += 1


def query_data(df: pd.DataFrame) -> pd.DataFrame:
    df["bill_to_tip"] = (
        (100 * df["total_bill"]).astype(int).astype(str)
        + "-"
        + (100 * df["tip"]).astype(int).astype(str)
    )
    df["size_to_time"] = df["size"].astype(str) + "-" + df["time"].astype(str)
    df["selected"] = True

    for q in ["bill_to_tip", "size_to_time", "day"]:
        if st.session_state[f"{q}_query"]:
            df.loc[
                ~df[q].isin(st.session_state[f"{q}_query"]), "selected"
            ] = False

    return df


def main():
    initialize_state()

    st.title("Cross Filter")

    df = load_data()
    query_data(df)

    render_preview_ui(df)
    current_query = render_plotly_ui(df)
    update_state(current_query)

    st.button("Reser filters", on_click=reset_state_callback)


main()
