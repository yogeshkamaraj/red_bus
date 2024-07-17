import mysql.connector
import pandas as pd
import streamlit as st
import pandas as pd
import streamlit_pandas as sp
 
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3306",
    password="Pepper4630",
    database="redbus" 
)
 
table_name='red_bus'
cursor = conn.cursor()
writer = cursor 
query = "SELECT * FROM red_bus"
writer.execute(query)
view = cursor.fetchall()
columns = [desc[0] for desc in writer.description]
data = pd.DataFrame(view, columns=columns)
data=data.set_index('s_no')



create_data = {
    "route-collected": "multiselect",
    "name": "text",
    "type": "multiselect",}

all_widgets = sp.create_widgets(data, create_data, ignore_columns=["departure_time", "arrival_time", "duration", "seats_available"])
res = sp.filter_df(data, all_widgets)

st.title("Red_Bus_Details")
st.header("Red_Bus")
st.write(data)
st.header("Filtered_Bus")
st.write(res)