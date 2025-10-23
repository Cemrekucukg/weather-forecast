import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import requests

# ------------------------------
# 🌤️ App Configuration
# ------------------------------
st.set_page_config(page_title="🌤️ Weather App", page_icon="☀️")

st.title("🌤️ Weather Temperature Prediction App")
st.write("Enter weather parameters below to predict the temperature.")

# ------------------------------
# 🔹 1. Download model from Google Drive
# ------------------------------
DRIVE_ID = "12JoXiG2YFTtXJ-t7Fo_mDRxhGqOHNGoc"  # ✅ Cemre'nin Drive ID'si
MODEL_URL = f"https://drive.google.com/uc?export=download&id={DRIVE_ID}"
MODEL_PATH = "weather_model.joblib"

if not os.path.exists(MODEL_PATH):
    st.info("📦 Downloading model from Google Drive...")
    try:
        r = requests.get(MODEL_URL)
        r.raise_for_status()
        with open(MODEL_PATH, "wb") as f:
            f.write(r.content)
        st.success("✅ Model downloaded successfully!")
    except Exception as e:
        st.error(f"❌ Error downloading model: {e}")

# ------------------------------
# 🔹 2. Load model safely
# ------------------------------
model = None
try:
    model = joblib.load(MODEL_PATH)
    st.success("✅ Model loaded successfully and ready to predict!")
except FileNotFoundError:
    st.error("⚠️ Model file not found. Please ensure the Google Drive ID is correct.")
except Exception as e:
    st.error(f"❌ Error while loading model: {e}")

# ------------------------------
# 🔹 3. User Input Section
# ------------------------------
st.subheader("🌦️ Enter Weather Parameters")

humidity = st.slider("Humidity (%)", 0, 100, 50)
wind_speed = st.slider("Wind Speed (km/h)", 0, 150, 10)
pressure = st.slider("Pressure (hPa)", 900, 1100, 1013)

# ------------------------------
# 🔹 4. Prediction Section
# ------------------------------
if st.button("🔮 Predict Temperature"):
    if model is None:
        st.warning("⚠️ Model not loaded, please check the configuration.")
    else:
        try:
            X_new = np.array([[humidity, wind_speed, pressure]])
            prediction = model.predict(X_new)[0]
            st.metric("🌡️ Predicted Temperature (°C)", f"{prediction:.2f}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
