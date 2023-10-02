import pandas as pd
import plotly.express as px
import streamlit as st
from components.streamlit_plotly_events.src import st_plotly_events
from plotly import graph_objects as go


def render_preview_ui(df: pd.DataFrame):
    with st.expander("Preview"):
        st.dataframe(df)


def build_bill_to_tip_figure(df: pd.DataFrame) -> go.Figure:
    fig = px.scatter(
        df,
        x="total_bill",
        y="tip",
        color="selected",
        hover_data=["total_bill", "tip", "day"],
        height=800,
        title="Total Bill vs Tip",
        template="seaborn",
    )
    return fig


def build_size_to_time_figure(df: pd.DataFrame) -> go.Figure:
    return px.density_heatmap(
        df[df["selected"] == True],
        x="size",
        y="time",
        height=400,
        template="seaborn",
    )


def build_day_figure(df: pd.DataFrame) -> go.Figure:
    return px.histogram(
        df, x="day", color="selected", height=400, template="seaborn"
    )


def render_plotly_ui(df: pd.DataFrame):
    bill_to_tip_figure = build_bill_to_tip_figure(df)
    size_to_time_figure = build_size_to_time_figure(df)
    day_figure = build_day_figure(df)

    c1, c2 = st.columns(2)

    with c1:
        bill_to_tip_selected = st_plotly_events(
            bill_to_tip_figure,
            select_event=True,
            click_event=False,
            hover_event=False,
            key=f"bill_to_tip_{st.session_state['counter']}",
        )
    with c2:
        size_to_time_clicked = st_plotly_events(
            size_to_time_figure,
            click_event=True,
            select_event=False,
            hover_event=False,
            key=f"size_to_time_{st.session_state['counter']}",
        )
        day_clicked = st_plotly_events(
            day_figure,
            click_event=True,
            hover_event=False,
            select_event=False,
            key=f"day_{st.session_state['counter']}",
        )

    current_query = {}
    current_query["bill_to_tip_query"] = {
        f"{int(100*el['x'])}-{int(100*el['y'])}"
        for el in bill_to_tip_selected
        if el
    }

    current_query["size_to_time_query"] = {
        f"{el['x']}-{el['y']}" for el in size_to_time_clicked
    }

    current_query["day_query"] = {el["x"] for el in day_clicked}

    # st.write(bill_to_tip_selected)
    # st.write(size_to_time_clicked)
    # st.write(day_clicked)

    return current_query
