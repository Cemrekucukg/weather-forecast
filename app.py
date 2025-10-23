import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import requests

st.set_page_config(page_title="🌤️ Weather App", page_icon="☀️")

st.title("🌤️ Weather Temperature Prediction App")
st.write("Enter weather conditions below to get a temperature prediction.")

# ------------------------------
# 🔹 1. Model download from Google Drive
# ------------------------------
DRIVE_ID = "13i2gE2UGZD-4oomAa8iZOZqqGG8iJW8d" 
MODEL_URL = f"https://drive.google.com/uc?export=download&id={DRIVE_ID}"
MODEL_PATH = "weather_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.info("📦 Downloading model from Google Drive...")
    r = requests.get(MODEL_URL)
    with open(MODEL_PATH, "wb") as f:
        f.write(r.content)
    st.success("✅ Model downloaded successfully!")

# ------------------------------
# 🔹 2. Load model safely
# ------------------------------
try:
    model = joblib.load(MODEL_PATH)
    st.success("✅ Model loaded and ready!")
except Exception as e:
    st.error(f"Model could not be loaded. Error: {e}")

# ------------------------------
# 🔹 3. Simple input form
# ------------------------------
st.subheader("Enter weather parameters:")
humidity = st.slider("Humidity (%)", 0, 100, 50)
wind_speed = st.slider("Wind Speed (km/h)", 0, 150, 10)
pressure = st.slider("Pressure (hPa)", 900, 1100, 1013)

if st.button("Predict Temperature"):
    X_new = np.array([[humidity, wind_speed, pressure]])
    try:
        prediction = model.predict(X_new)[0]
        st.metric("Predicted Temperature (°C)", f"{prediction:.2f}")
    except Exception as e:
        st.warning(f"Prediction error: {e}")
