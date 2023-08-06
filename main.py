import pandas as pd
import plotly.express as px
import requests
import streamlit as st

from utils.number_format import format_number

st.set_page_config(layout="wide")

st.title("Dashboard de Vendas :shopping_trolley:")

url = "https://labdados.com/produtos"
response = requests.get(url)
data = pd.DataFrame.from_dict(response.json())

data["Data da Compra"] = pd.to_datetime(
    data["Data da Compra"], format="%d/%m/%Y"
)

states_revenue = data.groupby("Local da compra")[["Preço"]].sum()
states_revenue = (
    data.drop_duplicates(subset=["Local da compra"])[
        ["Local da compra", "lat", "lon"]
    ]
    .merge(states_revenue, left_on="Local da compra", right_index=True)
    .sort_values("Preço", ascending=False)
)

monthly_revenue = (
    data.set_index("Data da Compra")
    .groupby(pd.Grouper(freq="M"))[["Preço"]]
    .sum()
    .reset_index()
)
monthly_revenue["Ano"] = monthly_revenue["Data da Compra"].dt.year
monthly_revenue["Mes"] = monthly_revenue["Data da Compra"].dt.month_name()


fig_states_revenue_map = px.scatter_geo(
    states_revenue,
    lat="lat",
    lon="lon",
    scope="south america",
    size="Preço",
    color="Local da compra",
    hover_name="Local da compra",
    hover_data={"lat": False, "lon": False},
    size_max=50,
    template="seaborn",
    title="Receita por Estado",
)


fig_monthly_revenue = px.line(
    monthly_revenue,
    x="Mes",
    y="Preço",
    markers=True,
    range_y=(0, monthly_revenue.max()),
    color="Ano",
    line_dash="Ano",
    title="Receita Mensal",
)

fig_monthly_revenue.update_layout(yaxis_title="Receita")

col1, col2 = st.columns(2)

with col1:
    st.metric("Receita Total", format_number(data["Preço"].sum()))
    st.plotly_chart(fig_states_revenue_map, use_container_width=True)
with col2:
    st.metric("Quantidade de Vendas", format_number(data.shape[0], ""))
    st.plotly_chart(fig_monthly_revenue, use_container_width=True)

st.dataframe(data, use_container_width=True)
