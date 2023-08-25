from st_pages import Page, add_page_title, show_pages


def set_pages():
    pages = [
        Page(p["path"], p["title"], p["icon"])
        for p in [
            {
                "path": "app/src/main.py",
                "title": "Dashboard de Vendas",
                "icon": ":shopping_trolley:",
            },
            {
                "path": "app/src/pages/EDA.py",
                "title": "Análise Exploratória de Dados",
                "icon": ":bar_chart:",
            },
            {
                "path": "app/src/pages/Detalhe.py",
                "title": "Dados Brutos",
                "icon": ":page_facing_up:",
            },
        ]
    ]
    show_pages(pages)
