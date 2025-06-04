import streamlit as st
import pandas as pd

st.header("*Macro Economic Data Analysis*", divider="gray")
st.markdown(
    """This platform empowers users to analyze and forecast macroeconomic trends using time series models. 
    Designed for researchers, analysts, and policymakers, the application combines classical statistical methods 
    with modern ML techniques to improve accuracy and interpretability."""
)
st.markdown(
    """Features include automated data preprocessing, visualization, feature engineering, and model evaluation. The 
    system enhances economic decision-making by enabling scenario analysis, trend detection, and early warning capabilities 
    through a user-friendly, modular interface tailored for macroeconomic data exploration."""
)

if st.button("Data Load"):
    st.switch_page("load-data.py")
