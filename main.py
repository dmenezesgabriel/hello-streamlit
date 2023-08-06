import pandas as pd
import plotly.express as px
import requests
import streamlit as st

from utils.number_format import format_number

st.set_page_config(
    layout="wide",
    page_title="Dashboard de Vendas",
    page_icon=":shopping_trolley:",
)

st.title("Dashboard de Vendas :shopping_trolley:")

url: str = "https://labdados.com/produtos"
regions = ["TODOS", "Centro-Oeste", "Nordeste", "Norte", "Sudeste", "Sul"]

st.sidebar.title("Filtros")
# Filters
region = st.sidebar.selectbox("Região", regions)
if region == "TODOS":
    region = ""

all_years = st.sidebar.checkbox("Dados de todo período", True)
if all_years:
    year = ""
else:
    year = st.sidebar.slider("Ano", 2020, 2023)

query_string = {"regiao": region.lower(), "ano": year}
response: requests.Response = requests.get(url, params=query_string)
data: pd.DataFrame = pd.DataFrame.from_dict(response.json())

sellers_filter = st.sidebar.multiselect(
    "Vendedores", data["Vendedor"].unique()
)
if sellers_filter:
    data = data[data["Vendedor"].isin(sellers_filter)]


# Data Cleaning
data["Data da Compra"] = pd.to_datetime(
    data["Data da Compra"], format="%d/%m/%Y"
)

states_revenue: pd.DataFrame = data.groupby("Local da compra")[["Preço"]].sum()
states_revenue = (
    data.drop_duplicates(subset=["Local da compra"])[
        ["Local da compra", "lat", "lon"]
    ]
    .merge(states_revenue, left_on="Local da compra", right_index=True)
    .sort_values("Preço", ascending=False)
)

monthly_revenue: pd.DataFrame = (
    data.set_index("Data da Compra")
    .groupby(pd.Grouper(freq="M"))[["Preço"]]
    .sum()
    .reset_index()
)
monthly_revenue["Ano"] = monthly_revenue["Data da Compra"].dt.year
monthly_revenue["Mes"] = monthly_revenue["Data da Compra"].dt.month_name()

categories_revenue: pd.DataFrame = (
    data.groupby("Categoria do Produto")[["Preço"]]
    .sum()
    .sort_values("Preço", ascending=False)
)

sellers: pd.DataFrame = pd.DataFrame(
    data.groupby("Vendedor")["Preço"].agg({"sum", "count"})
)

# Figures
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

fig_states_revenue = px.bar(
    states_revenue.head(5),
    x="Local da compra",
    y="Preço",
    text_auto=True,
    color="Local da compra",
    title="TOP Receita por Estado",
)

fig_states_revenue.update_layout(yaxis_title="Receita")

fig_categories_revenue = px.bar(
    categories_revenue, text_auto=True, title="Receita por Categoria"
)

fig_categories_revenue.update_layout(yaxis_title="Receita")

# UI
tab1, tab2, tab3 = st.tabs(["Receita", "Quantidade de vendas", "Vendedores"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Receita Total", format_number(data["Preço"].sum()))
        st.plotly_chart(fig_states_revenue_map, use_container_width=True)
        st.plotly_chart(fig_states_revenue, use_container_width=True)
    with col2:
        st.metric("Quantidade de Vendas", format_number(data.shape[0], ""))
        st.plotly_chart(fig_monthly_revenue, use_container_width=True)
        st.plotly_chart(fig_categories_revenue, use_container_width=True)

    st.dataframe(data, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Receita Total", format_number(data["Preço"].sum()))
    with col2:
        st.metric("Quantidade de Vendas", format_number(data.shape[0], ""))


with tab3:
    qty_sellers: int = st.number_input("Quantidade de vendedores", 1, 10, 5)
    fig_sellers_revenue = px.bar(
        sellers[["sum"]].sort_values("sum", ascending=False).head(qty_sellers),
        x="sum",
        y=sellers[["sum"]]
        .sort_values("sum", ascending=False)
        .head(qty_sellers)
        .index,
        text_auto=True,
        title=f"TOP {qty_sellers} Receita por Vendedor",
    )
    fig_sellers_sells = px.bar(
        sellers[["count"]]
        .sort_values("count", ascending=False)
        .head(qty_sellers),
        x="count",
        y=sellers[["count"]]
        .sort_values("count", ascending=False)
        .head(qty_sellers)
        .index,
        text_auto=True,
        title=f"TOP {qty_sellers} Vendas por Vendedor",
    )
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Receita Total", format_number(data["Preço"].sum()))
        st.plotly_chart(fig_sellers_revenue, use_container_width=True)
    with col2:
        st.metric("Quantidade de Vendas", format_number(data.shape[0], ""))
        st.plotly_chart(fig_sellers_sells, use_container_width=True)
