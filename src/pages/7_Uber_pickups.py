import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Uber Pickups",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATE_COLUMN = "date/time"
DATA_URL = (
    "https://s3-us-west-2.amazonaws.com/"
    "streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(lambda x: str(x).lower(), axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


def render_charts_ui(df: pd.DataFrame):
    col1, col2 = st.columns(2)

    st.subheader("Number of pickups by hour")

    with st.sidebar:
        hour_to_filter = st.slider("hour", 0, 23, 17)

    with col1:
        hist_values = np.histogram(
            df[DATE_COLUMN].dt.hour, bins=24, range=(0, 24)
        )[0]
        st.bar_chart(hist_values)

    with col2:
        filtered_data = df[df[DATE_COLUMN].dt.hour == hour_to_filter]
        st.map(filtered_data)
        filtered_data.shape[0]


def render_raw_data_ui(df: pd.DataFrame):
    with st.expander("show raw data"):
        st.write(df)


def main():
    st.title("Uber pickups in NYC")

    data_load_state = st.info("Loading data...")
    df = load_data(10000)
    data_load_state.empty()

    render_charts_ui(df)
    render_raw_data_ui(df)


main()
