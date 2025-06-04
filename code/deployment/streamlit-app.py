import streamlit as st

pages = {
    "Macro Economic Data Analysis": [
        st.Page("intro.py", title="Macro Economic Data Analysis"),
    ],
    "Data Load": [
        st.Page("load-data.py", title="Load Data"),
    ],
    "EDA": [
        st.Page("eda.py", title="EDA"),
    ],
}



pg = st.navigation(pages,position="hidden")
pg.run()
