import streamlit as st
import pandas as pd
from dataset import load_data, write_data, CATEGORY_LIST

data1 = load_data("data1")
data2 = load_data("data2")
total_data = pd.concat([data1, data2])
st.title("Data Visualization")
st.write(
    "**category**: data label    \n"
    "**data_id**: 1.txt, 2.txt, etc. each represent a single time series data.   \n"
    "**time_step**: It represents the time axis in a single data set"
)
st.dataframe(total_data)

category = st.pills("Select Category", options=CATEGORY_LIST)
if category:
    category_df = total_data[total_data["category"] == category]
    data_id_list = sorted(category_df["data_id"].unique())
    data_id = st.pills("Select Data Id", options=data_id_list)
    if data_id:
        st.pyplot(write_data(total_data, category, data_id))
