import streamlit as st
from components.streamlit_pure_javascript_component import st_pure_js_input


st.set_page_config(
    page_title="Pure Javascript Component",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Pure Javascript Component")


def run_component(props):
    value = st_pure_js_input(key="example", **props)
    return value


def handle_event(value):
    st.header("Streamlit")
    st.write("Received from component: ", value)


def main():
    props = {
        "initial_state": {"message": "Hello! Enter some text"},
    }

    handle_event(run_component(props))
    st.title("Component Example")


main()
