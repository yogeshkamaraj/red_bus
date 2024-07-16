import streamlit as st
import pandas as pd
import streamlit_pandas as sp

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    return df

file = "red_bus.csv"
df = load_data(file)

create_data = {
    "route-collected": "multiselect",
    "name": "multiselect",
    "type": "multiselect",
    "rating": "multiselect"
}

all_widgets = sp.create_widgets(df, create_data, ignore_columns=("s_no", "departure_time", "arrival_time", "duration", "seats_available"))
res = sp.filter_df(df, all_widgets)

st.title("Red_Bus_Details")
st.header("Red_Bus")
st.write(df)

st.header("Your_Result")
st.write(res)
