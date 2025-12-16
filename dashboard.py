import streamlit as st
import sqlite3
import pandas as pd

st.title("📊 Product Data Dashboard")

conn = sqlite3.connect("database.db")

df = pd.read_sql("SELECT * FROM products", conn)
status = pd.read_sql("SELECT * FROM pipeline_status", conn)

st.metric("Total Products", len(df))
st.metric("Average Price (INR)", round(df["price_inr"].mean(), 2))

st.subheader("Pipeline Status")
st.write(status)

st.subheader("Products")
st.dataframe(df)

st.subheader("Average Price by Category")
chart = df.groupby("category")["price_inr"].mean()
st.bar_chart(chart)
