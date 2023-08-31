import random
from datetime import datetime, time

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Hello, World!",
    page_icon=":sunglasses:",
    layout="wide",
    initial_sidebar_state="expanded",
)


def render_text_ui():
    st.title("Hello, World!")

    st.header("This is a header", help="This is a tooltip", divider="rainbow")

    st.markdown(
        """
        This is a :rainbow[Markdown]
        """
    )

    st.subheader(
        "This is a subheader", help="This is a tooltip", divider="gray"
    )

    st.code(
        """
        import streamlit as st

        st.write("Hello, World!")
        """,
        language="python",
        line_numbers=True,
    )

    st.text("This is a text", help="This is a tooltip")

    st.latex(
        r"""
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        """
    )

    st.caption("This is a caption", help="This is a tooltip")

    st.divider()


@st.cache_data
def get_random_stars():
    return [random.randint(0, 1000) for _ in range(3)]


@st.cache_data
def get_random_views_history():
    return [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)]


def render_dataframe_ui():
    st.header("Table", help="This is a tooltip", divider="rainbow")

    st.info("Edit Me!")

    df = pd.DataFrame(
        {
            "name": ["Roadmap", "Extras", "Issues"],
            "url": [
                "https://roadmap.streamlit.app",
                "https://extras.streamlit.app",
                "https://issues.streamlit.app",
            ],
            "stars": get_random_stars(),
            "views_history": get_random_views_history(),
            "isActive": [True, False, True],
            "widgets": ["🗺", "🎁", "🐞"],
            "category": [
                "📊 Data Exploration",
                "📈 Data Visualization",
                "📊 Data Exploration",
            ],
            "appointment": [
                datetime(2024, 2, 5, 12, 30),
                datetime(2023, 11, 10, 18, 0),
                datetime(2024, 3, 11, 20, 10),
            ],
            "time": [
                time(12, 30),
                time(18, 0),
                time(9, 10),
            ],
            "images": [
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            ],
            "sales": [200, 550, 1000],
        }
    )

    edited_df = st.data_editor(
        df,
        column_config={
            "name": st.column_config.TextColumn(
                "App name",
                validate="^[a-z]",
                help="Only String characters are allowed",
            ),
            "stars": st.column_config.NumberColumn(
                "Github stars",
                help="This is a tooltip",
                format="%d ⭐",
            ),
            "url": st.column_config.LinkColumn(
                "App URL", help="This is a tooltip"
            ),
            "views_history": st.column_config.LineChartColumn(
                "Views history (past 30 days)",
                y_min=0,
                y_max=5000,
                help="This is a tooltip",
            ),
            "widgets": st.column_config.Column(
                "Icons",
                help="Help 🎈",
                width="medium",
            ),
            "category": st.column_config.SelectboxColumn(
                "select option",
                options=[
                    "📊 Data Exploration",
                    "📈 Data Visualization",
                    "📊 Data Exploration",
                ],
                help="This is a tooltip",
            ),
            "appointment": st.column_config.DatetimeColumn(
                "datetime",
                min_value=datetime(2021, 1, 1),
                max_value=datetime(2025, 1, 1),
                format="YYYY/MM/DD - hh:mm",
                help="This is a tooltip",
            ),
            "time": st.column_config.TimeColumn(
                "time",
                min_value=time(0, 0),
                max_value=time(23, 59),
                format="hh:mm a",
                help="This is a tooltip",
            ),
            "images": st.column_config.ImageColumn(
                "images",
                help="This is a tooltip",
            ),
            "sales": st.column_config.ProgressColumn(
                "sales",
                min_value=0,
                max_value=1000,
                format="$%f",
                help="This is a tooltip",
            ),
        },
        hide_index=True,
        use_container_width=True,
        num_rows="dynamic",
        key="editor",
    )

    st.text("output (dataframe):")
    st.dataframe(edited_df)
    st.text("output (static table):")
    st.table(edited_df)


def render_json_ui():
    st.header("JSON", help="This is a tooltip", divider="gray")
    st.json(
        {
            "foo": "bar",
            "baz": "boz",
            "stuff": [
                "stuff 1",
                "stuff 2",
                "stuff 3",
                "stuff 5",
            ],
        }
    )


def render_metric_ui():
    st.header("Metrics", help="This is a tooltip", divider="blue")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Temperature", value="70 °F", delta="2 °F")
    with col2:
        st.metric(label="Humidity", value="50 %", delta="5 %")
    with col3:
        st.metric(label="Pressure", value="1000 hPa", delta="10 hPa")
    with col4:
        st.metric(label="Wind", value="10 km/h", delta="2 km/h")


@st.cache_data
def get_random_chart_data():
    return pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"],
    )


def render_chart_ui():
    st.header("Native Charts", help="This is a tooltip", divider="violet")
    data = get_random_chart_data()

    with st.expander("data"):
        st.dataframe(data)

    st.subheader("Line Chart")
    st.line_chart(data)
    st.subheader("Area Chart")
    st.area_chart(data)
    st.subheader("Bar Chart")
    st.bar_chart(data)


def main():
    render_text_ui()
    render_dataframe_ui()
    render_json_ui()
    render_metric_ui()
    render_chart_ui()


main()
