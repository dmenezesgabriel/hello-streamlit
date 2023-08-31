import os

import streamlit.components.v1 as components

component_example = components.declare_component(
    name="example", path=f"{os.path.dirname(__file__)}/frontend"
)
