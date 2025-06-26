import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Orders Manager", layout="wide")

# Load the Excel file
@st.cache_data
def load_data():
    return pd.read_excel("Orders.xlsx", engine="openpyxl")

df = load_data()

st.title("📦 Orders Management App")

# Show all orders
st.subheader("📋 Existing Orders")
st.dataframe(df, use_container_width=True)

# Add a new order
st.subheader("➕ Add New Order")

with st.form("new_order_form"):
    date = st.date_input("Order Date", value=datetime.today())
    sno = st.text_input("S.NO")
    company = st.text_input("Company")
    item_size = st.text_input("Item Size")
    grade = st.text_input("Grade")
    thread_size = st.text_input("Thread Size")
    quantity = st.number_input("Quantity", min_value=1)
    unit = st.text_input("Unit")
    due_date = st.date_input("Due Date")
    purpose = st.text_area("Purpose")

    submitted = st.form_submit_button("Save Order")

    if submitted:
        new_order = {
            "Order ID": f"ORD{len(df)+1:04d}",
            "DATE": date,
            "S.NO": sno,
            "Company": company,
            "Item size": item_size,
            "Grade": grade,
            "Thread Size": thread_size,
            "Quantity": quantity,
            "Unit": unit,
            "Due date": due_date,
            "Purpose": purpose
        }

        df = pd.concat([df, pd.DataFrame([new_order])], ignore_index=True)
        df.to_excel("Orders.xlsx", index=False)
        st.success("✅ Order added successfully! Reload the app to see the update.")