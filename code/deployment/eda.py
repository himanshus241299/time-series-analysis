import streamlit as st
import pandas as pd
import numpy as np
import utilities as utils
import altair as alt

st.header("*EDA*", divider="gray")

df = st.session_state["data"]
summary_df = st.session_state["summary_data"]

mev = st.selectbox(
    "Macro Economic Variable",
    list(summary_df["Macro Variable"]),
    index=None,
    placeholder="Select a macro economic variable",
    accept_new_options=True,
)
if mev is not None:
    st.write(
        "Macroeconomic Variable: ",
        summary_df[summary_df["Macro Variable"] == mev]["Description"].values[0],
    )
    st.write(
        "Time Range: ",
        summary_df[summary_df["Macro Variable"] == mev]["Time Range"].values[0],
    )
    st.write(
        "Source: ",
        summary_df[summary_df["Macro Variable"] == mev]["Description"].values[0],
    )

    trans_options = ["Raw", "Difference", "Growth", "Log", "Log Difference"]
    transf = st.pills(
        "Transformation", trans_options, selection_mode="single", default="Raw"
    )

    series = df[2:][["Macro Variable", mev]]
    series.columns = ["time_key", "raw"]
    series["raw"] = pd.to_numeric(series["raw"], errors="coerce")
    if transf == "Raw":
        series["value"] = series["raw"]
    elif transf == "Difference":
        series["value"] = series["raw"].diff()
    elif transf == "Growth":
        series["value"] = series["raw"].pct_change() * 100
    elif transf == "Log":
        series["value"] = series["raw"].apply(lambda x: np.log(x) if x > 0 else np.nan)
    elif transf == "Log Difference":
        series["value"] = (
            series["raw"].apply(lambda x: np.log(x) if x > 0 else np.nan).diff()
        )

    time_series = (
        alt.Chart(series)
        .mark_line(interpolate="monotone")
        .encode(x="time_key:T", y="value", color="symbol:N")
        .interactive()
    )

    hist = (
        alt.Chart(series)
        .mark_bar()
        .encode(
            alt.X("value").bin(maxbins=100),
            alt.Y("count()"),
            alt.Color("value").bin(maxbins=100).scale(scheme="pinkyellowgreen"),
        )
        .interactive()
    )

    tab1, tab2, tab3 = st.tabs(["Time Series", "Histogram", "Decomposition"])

    with tab1:
        st.altair_chart(time_series, theme="streamlit", use_container_width=True)
    with tab2:
        st.altair_chart(hist, theme=None, use_container_width=True)
