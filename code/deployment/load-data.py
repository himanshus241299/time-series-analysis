import streamlit as st
import pandas as pd
import utilities as utils

st.header("*Load Data*", divider="gray")


st.subheader("*Data Format*")

st.caption("Please Upload Data in following format")
sample_data = pd.read_excel("data/input/sample_mev_data.xlsx")
st.dataframe(sample_data, hide_index=True)

uploaded_file = st.file_uploader(
    label="Upload Data", type=["csv", "xlsx"], label_visibility="hidden"
)
if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

summary_df = utils.summary(df)

st.subheader("*Data Summary*")

st.data_editor(
    summary_df,
    column_config={
        "Values": st.column_config.LineChartColumn(
            "Time Series",
            width="medium",
            y_min=0,
            y_max=100,
        ),
        "Select": st.column_config.CheckboxColumn(
            "Select",
            help="Select your **favorite** widgets",
            default=True,
        ),
    },
    hide_index=True,

)

if st.button("Exploratory Data Analysis"):
    st.switch_page("eda.py")
