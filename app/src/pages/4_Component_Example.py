import streamlit as st
from components.example import component_example


def run_component(props):
    value = component_example(key="example", **props)
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
