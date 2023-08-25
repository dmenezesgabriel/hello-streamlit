from ui.eda import upload_sheet, view_sheet
from utils.page import setup_page

setup_page("EDA")

uploaded_file = upload_sheet()
view_sheet(uploaded_file)
