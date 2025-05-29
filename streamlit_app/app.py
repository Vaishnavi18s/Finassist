import streamlit as st
import requests

st.title("📈 Multi-Agent Finance Assistant")
query = st.text_input("Ask your finance question:")

if st.button("Submit"):
    res = requests.post("http://localhost:8000/orchestrate", json={"query": query})
    st.write(res.json()["response"])