import streamlit as st
import requests

st.title("Penguin Species Predictor")

st.write("Enter the penguin features below to predict its species:")

bill_length_mm = st.number_input("Bill Length (mm)", min_value=0.0, max_value=100.0, value=43.2, step=0.1)
bill_depth_mm = st.number_input("Bill Depth (mm)", min_value=0.0, max_value=30.0, value=17.0, step=0.1)
flipper_length_mm = st.number_input("Flipper Length (mm)", min_value=0.0, max_value=300.0, value=200.0, step=1.0)
body_mass_g = st.number_input("Body Mass (g)", min_value=0.0, max_value=10000.0, value=4000.0, step=10.0)

prediction_placeholder = st.empty()

if st.button("Predict"):
    input_data = {
        "bill_length_mm": bill_length_mm,
        "bill_depth_mm": bill_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g": body_mass_g
    }
    
    api_url = "http://api-service:8000/predict"
    try:
        response = requests.post(api_url, json=input_data)
        if response.status_code == 200:
            species = response.json()['predicted_species']
            prediction_placeholder.success(f"The predicted species is: {species}")
        else:
            prediction_placeholder.error("Error occurred while making prediction.")
    except requests.exceptions.RequestException as e:
        prediction_placeholder.error(f"Error: Could not connect to API. Details: {e}")