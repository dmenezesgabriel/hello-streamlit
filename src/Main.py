import random
from datetime import datetime, time

import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from vega_datasets import data

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
    chart_data = get_random_chart_data()

    with st.expander("data"):
        st.dataframe(chart_data)

    st.subheader("Line Chart")
    st.line_chart(chart_data)
    st.subheader("Area Chart")
    st.area_chart(chart_data)
    st.subheader("Bar Chart")
    st.bar_chart(chart_data)


def render_matplotlib_ui():
    st.header("Matplotlib", help="This is a tooltip", divider="green")

    col1, col2, col3 = st.columns(3)

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    with col1:
        st.pyplot(fig, clear_figure=True, use_container_width=True)


def render_altair_basic_ui():
    st.header("Altair", help="This is a tooltip", divider="red")

    chart_data = get_random_chart_data()

    chart = (
        alt.Chart(chart_data)
        .mark_circle()
        .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
    )

    st.altair_chart(chart, use_container_width=True)

    source = data.cars()

    with st.expander("data"):
        st.dataframe(source)

    chart = (
        alt.Chart(source)
        .mark_circle()
        .encode(x="Horsepower", y="Miles_per_Gallon", color="Origin")
    ).interactive()

    tab1, tab2 = st.tabs(["Streamlit native theme", "Altair native theme"])

    with tab1:
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
    with tab2:
        st.altair_chart(chart, theme=None, use_container_width=True)


def render_altair_advanced_ui():
    st.header("Altair advanced", help="This is a tooltip", divider="red")

    source = data.seattle_weather()

    with st.expander("data"):
        st.dataframe(source)

    scale = alt.Scale(
        domain=["sun", "fog", "drizzle", "rain", "snow"],
        range=["#e7ba52", "#c7c7c7", "#aec7e8", "#1f77b4", "#9467bd"],
    )

    color = alt.Color("weather:N", scale=scale)
    brush = alt.selection_interval(encodings=["x"])
    click = alt.selection_multi(encodings=["color"])

    points = (
        alt.Chart()
        .mark_point()
        .encode(
            alt.X("monthdate(date):T", title="Date"),
            alt.Y(
                "temp_max:Q",
                title="Maximum Daily Temperature(C)",
                scale=alt.Scale(domain=[-5, 40]),
            ),
            color=alt.condition(brush, color, alt.value("lightgray")),
            size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
        )
        .properties(width=600, height=300)
        .add_selection(brush)
        .transform_filter(click)
    )

    bars = (
        alt.Chart()
        .mark_bar()
        .encode(
            x="count()",
            y="weather:N",
            color=alt.condition(click, color, alt.value("lightgray")),
        )
        .transform_filter(brush)
        .properties(width=600)
        .add_selection(click)
    )

    chart = alt.vconcat(
        points, bars, data=source, title="Seattle Weather: 2012-2015"
    )

    st.altair_chart(chart, theme="streamlit", use_container_width=True)


def render_vega_lite_ui():
    st.header("Vega Lite", help="This is a tooltip", divider="gray")

    chart_data = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

    st.vega_lite_chart(chart_data, {
        'mark': {'type': 'circle', 'tooltip': True},
        'encoding': {
            'x': {'field': 'a', 'type': 'quantitative'},
            'y': {'field': 'b', 'type': 'quantitative'},
            'size': {'field': 'c', 'type': 'quantitative'},
            'color': {'field': 'c', 'type': 'quantitative'},
        },
    })


def main():
    render_text_ui()
    render_dataframe_ui()
    render_json_ui()
    render_metric_ui()
    render_chart_ui()
    render_matplotlib_ui()
    render_altair_basic_ui()
    render_altair_advanced_ui()
    render_vega_lite_ui()


main()
