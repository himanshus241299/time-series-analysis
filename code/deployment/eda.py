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

st.subheader("*Upload Data*")

st.caption("Please Upload Data in following format")
sample_data = pd.read_excel("data/input/sample_mev_data.xlsx")
st.dataframe(sample_data, use_container_width=True)

uploaded_file = st.file_uploader(
    label="Upload Data", type=["csv", "xlsx"], label_visibility="hidden"
)
if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    st.dataframe(df)
    st.markdown("**")
