import pandas as pd
import numpy as np
import os

# os.chdir("C:/Users/himan/Desktop/TSA/time-series-analysis/data/input")

# df = pd.read_excel("sample_mev_data.xlsx")


def summary(df):
    summary_df = df.transpose().reset_index()
    summary_df.columns = summary_df.iloc[0]
    summary_df = summary_df[1:]

    summary_df["Values"] = summary_df.iloc[:, 3:].values.tolist()
    summary_df["#Observations"] = summary_df["Values"].apply(
        lambda x: len(x) if isinstance(x, list) else 0
    )
    summary_df["Select"] = True
    return summary_df[
        ["Select", "Macro Variable", "Description", "Time Range", "#Observations","Values"]
    ]
