import streamlit as st
import pandas as pd
import numpy as np
import joblib
import urllib.request
import os

# 🎯 Google Drive'dan model dosyasını otomatik indir
MODEL_URL = "https://drive.google.com/uc?export=download&id=13i2gE2UGZD-4oomAa8iZOZqqGG8iJW8d"
MODEL_PATH = "weather_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.info("📦 Downloading model from Google Drive...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

model = joblib.load(MODEL_PATH)
st.title("🌤️ Weather Temperature Prediction App")

st.write("Enter the weather parameters below to predict the temperature:")


humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=50)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=100.0, value=10.0)
pressure = st.number_input("Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1013.0)
visibility = st.number_input("Visibility (km)", min_value=0.0, max_value=50.0, value=10.0)

# 📈 Tahmin butonu
if st.button("Predict Temperature"):
    input_data = np.array([[humidity, wind_speed, pressure, visibility]])
    prediction = model.predict(input_data)
    st.success(f"🌡️ Predicted Temperature: {prediction[0]:.2f} °C")
