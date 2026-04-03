import pickle

import numpy as np
import streamlit as st

model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Crop Recommendation", layout="centered")

st.title(" Crop Recommendation System")

st.write("Provide soil and environmental details:")


col1, col2 = st.columns(2)

with col1:
    N = st.slider("Nitrogen (N)", 0, 200, 50)
    P = st.slider("Phosphorus (P)", 0, 200, 50)
    K = st.slider("Potassium (K)", 0, 200, 50)
    temperature = st.slider("Temperature (°C)", 0.0, 50.0, 25.0)

with col2:
    humidity = st.slider("Humidity (%)", 0.0, 100.0, 50.0)
    ph = st.slider("pH Level", 0.0, 14.0, 6.5)
    rainfall = st.slider("Rainfall (mm)", 0.0, 300.0, 100.0)


if st.button(" Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]

    st.success(f" Recommended Crop: {prediction}")


st.subheader(" About Model")
st.write(
    """
- Model: Random Forest Classifier  
- Uses soil nutrients + environmental factors  
- Provides real-time crop recommendations  
"""
)


st.markdown("---")
st.write("Developed by Simhadri Kondapally ")
