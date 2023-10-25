import streamlit as st
from components.streamlit_gtag import st_gtag


st.set_page_config(
    page_title="Google Gtag",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Google GtagJs :chart:")


def main():
    st_gtag(
        key="gtag_send_event_a",
        id="G-LDSKH1L6V2",
        mode="event",
        event_name="dummy_test",
        params={
            "event_category": "test_category",
            "event_label": "test_label",
            "value": 96,
        },
    )

    st_gtag(
        key="st_gtag_set_b",
        id="G-LDSKH1L6V2",
        mode="set",
        params={"country": "US", "currency": "USD"},
    )


main()
