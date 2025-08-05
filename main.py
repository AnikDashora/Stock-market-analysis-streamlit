import streamlit as st
from landing_page import landingpage
from dashborad_page import dashboard
from data_funtions import initilaze
# def set_stock_data_file(stock_name):
#     st.session_state["current_page"] = "dashbord_page"
#     st.session_state["current_stock"] = stock_name
#     st.session_state["current_stock_file_path"] = f"D:\\project-3\\stock_market_data\\{stock_name}_DATA_SET.csv"

initilaze()

if(st.session_state["current_page"] == "landing_page"):
    landingpage()
if(st.session_state["current_page"] == "dashbord_page"):
    dashboard()


if __name__ == "__main__":
    pass
