import streamlit as st
import requests

st.title("HTS Special Rate Eligibility Predictor")

# Input fields
Indent = st.number_input("Indent", min_value=0)
Description = st.text_input("Description")
Unit_of_Quantity = st.text_input("Unit of Quantity")
Chapter = st.text_input("Chapter")
Country_of_Origin = st.text_input("Country of Origin")
heading_code = st.text_input("Heading Code")
subheading_code = st.text_input("Subheading Code")
hts_length = st.number_input("HTS Length", min_value=0)

if st.button("Predict"):
    payload = {
        "Indent": Indent,
        "Description": Description,
        "Unit_of_Quantity": Unit_of_Quantity,
        "Chapter": Chapter,
        "Country_of_Origin": Country_of_Origin,
        "heading_code": heading_code,
        "subheading_code": subheading_code,
        "hts_length": hts_length
    }
    headers = {"x-api-key": "htfb-lijm-sdfer-aov"}
    response = requests.post("http://127.0.0.1:8000/predict/", json=payload, headers=headers)
    if response.status_code == 200:
        st.success(f"Prediction: {response.json()['prediction']}")
    else:
        st.error(f"Error: {response.text}")