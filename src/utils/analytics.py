import datetime
import inspect
import json
from contextlib import contextmanager
from pathlib import Path

import streamlit as st

from utils.server_headers import get_url

_st_button = st.button
_st_checkbox = st.checkbox
_st_radio = st.radio
_st_selectbox = st.selectbox
_st_multiselect = st.multiselect
_st_slider = st.slider
_st_select_slider = st.select_slider
_st_text_input = st.text_input
_st_number_input = st.number_input
_st_text_area = st.text_area
_st_date_input = st.date_input
_st_time_input = st.time_input
_st_file_uploader = st.file_uploader
_st_color_picker = st.color_picker
_st_expander = st.expander

_st_slider_button = st.sidebar.button
_st_slider_checkbox = st.sidebar.checkbox
_st_slider_radio = st.sidebar.radio
_st_slider_selectbox = st.sidebar.selectbox
_st_slider_multiselect = st.sidebar.multiselect
_st_slider_slider = st.sidebar.slider
_st_slider_select_slider = st.sidebar.select_slider
_st_slider_text_input = st.sidebar.text_input
_st_slider_number_input = st.sidebar.number_input
_st_slider_text_area = st.sidebar.text_area
_st_slider_date_input = st.sidebar.date_input
_st_slider_time_input = st.sidebar.time_input
_st_slider_file_uploader = st.sidebar.file_uploader
_st_slider_color_picker = st.sidebar.color_picker
_st_slider_expander = st.sidebar.expander


def replace_empty(value):
    if isinstance(value, str):
        return value if value and value != "" else "EMPTY"
    return value


def _wrap_button(func, store):
    def new_func(label, *args, **kwargs):
        clicked = func(label, *args, **kwargs)
        label = replace_empty(label)
        if label not in store:
            store[label] = {"counter": 0, "url": None}
        if clicked:
            store[label]["counter"] += 1
            store[label]["url"] = get_url()
            if "key" in kwargs:
                store[label]["key"] = kwargs["key"]
        return clicked

    return new_func


def start_tracking():
    if "st_analytics" not in st.session_state:
        st.session_state["st_analytics"] = {}
    if not "widgets" in st.session_state.st_analytics:
        st.session_state.st_analytics["widgets"] = {}
    widgets = st.session_state.st_analytics["widgets"]
    if "buttons" not in st.session_state.st_analytics["widgets"]:
        st.session_state.st_analytics["widgets"]["buttons"] = {}
    buttons = st.session_state.st_analytics["widgets"]["buttons"]

    st.button = _wrap_button(_st_button, buttons)


def stop_tracking():
    st.button = _st_button


@contextmanager
def st_track():
    start_tracking()

    yield
    stop_tracking()
