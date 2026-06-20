import streamlit as st
import pandas as pd
import os
import csv
from datetime import datetime

# Page Setup
st.set_page_config(page_title="Personal Expense Tracker", page_icon="💰")

st.title("💰 Daily Expense Ledger")
st.caption("Keep track of every penny for Mummy's records.")
st.write("---")

# Data File Path
DATA_FILE = "personal_expenses.csv"

# Input Form
with st.form("add_expense", clear_on_submit=True):
    col1, col2 = st.columns(2)
    item = col1.text_input("What did you buy?")
    amount = col2.number_input("Amount (₹)", min_value=0.0, step=5.0)
    category = st.selectbox("Category", ["Food", "Transport", "Medicine", "Stationery", "Other"])
    
    if st.form_submit_button("Log Expense"):
        if item and amount > 0:
            with open(DATA_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now().strftime("%Y-%m-%d"), item, amount, category])
            st.success(f"Added {item} - ₹{amount}")
        else:
            st.warning("Please enter a valid item and amount.")

# Display and Summary
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE, names=["Date", "Item", "Amount", "Category"])
    
    st.write("---")
    st.subheader("📊 Your Spending Summary")
    
    # Simple summary table
    st.dataframe(df.sort_index(ascending=False), use_container_width=True)
    
    # Calculate Totals
    total_spent = df['Amount'].sum()
    st.metric("Total Spent So Far", f"₹{total_spent:,.2f}")
    
    # Category Analysis
    if st.checkbox("Show category breakdown"):
        st.bar_chart(df.groupby("Category")["Amount"].sum())
else:
    st.info("No expenses logged yet. Start adding your first item above!")

# Optional: Clear data button
if st.button("Clear All Data"):
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
        st.rerun()