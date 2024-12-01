import os
import streamlit as st
import csv
import json

st.header("Conversation History")
# with st.beta_expander("Click to see Conversation History"):
with open('chat_history.csv', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        st.text(f"User: {row[0]}")
        st.text(f"Isayu: {row[1]}")
        st.text(f"Timestamp: {row[2]}")
        st.markdown("---")