import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("weather_model.pkl")

st.title("🌤️ Weather Temperature Prediction App")
st.write("Enter weather conditions below to get a temperature prediction:")

# User inputs
humidity = st.slider("Humidity (%)", 0, 100, 50)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=50.0, value=10.0)
visibility = st.number_input("Visibility (km)", min_value=0.0, max_value=20.0, value=10.0)
pressure = st.number_input("Pressure (millibars)", min_value=900.0, max_value=1100.0, value=1013.0)

# Predict button
if st.button("Predict Temperature"):
    input_data = np.array([[humidity/100, wind_speed, visibility, pressure]])
    prediction = model.predict(input_data)[0]
    st.success(f"🌡️ Predicted Temperature: {prediction:.2f} °C")
