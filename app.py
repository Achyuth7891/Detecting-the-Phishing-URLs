import streamlit as st
from malicious_ml_feat_engg import get_prediction_from_url

def predict_url(url):
    if url:
        prediction = get_prediction_from_url(url)
        st.success(f"The URL '{url}' is predicted as '{prediction}'")
    else:
        st.warning("Please enter a URL.")

# Create UI components
st.title("URL Predictor")
url_input = st.text_input("Enter URL:")
predict_button = st.button("Predict")

# Perform prediction on button click
if predict_button:
    predict_url(url_input)
