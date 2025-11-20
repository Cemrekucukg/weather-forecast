# 🌤️ Weather Forecast - Machine Learning Model

This repository contains a **machine learning-based weather temperature prediction project**.  
It demonstrates a complete workflow from **data preprocessing and model training** (in Jupyter/Colab) to **deployment-ready packaging** (via Streamlit or API).

---

## 🧠 Project Overview
The model predicts **temperature (°C)** based on key atmospheric parameters:
- **Humidity (%)**
- **Wind Speed (km/h)**
- **Pressure (hPa)**

The model was trained and evaluated in Colab, then exported using `joblib`.  
The app component (`app.py`) is prepared for deployment with **Streamlit**, but **UI is currently disabled** for this version.

---

## 🧩 Repository Structure
📁 weather-forecast/
├── app.py # Streamlit app (UI disabled)
├── weather_prediction.ipynb # Notebook with full training pipeline
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── .gitignore # Ignore cache and large model files


---

## 🚀 Key Features
✅ Model training and evaluation notebook  
✅ Colab-compatible workflow (GPU supported)  
✅ Modular design for easy extension (API or web UI)  
✅ Ready-to-run Streamlit backend  
✅ Compatible with any regression dataset after retraining  

---

## 🧰 Tech Stack
- **Language:** Python 3.11  
- **Libraries:** pandas, numpy, scikit-learn, joblib, streamlit  
- **Environment:** Google Colab / VS Code  
- **Model Serialization:** `joblib`  

---

## 📓 Interactive Notebook
You can explore the model training, data processing, and evaluation steps below:

👉 [Open in Google Colab](https://colab.research.google.com/github/Cemrekucukg/weather-forecast/blob/main/weather_prediction.ipynb)

---

## ⚙️ How to Run Locally
```bash
# 1️⃣ Clone the repository
git clone https://github.com/Cemrekucukg/weather-forecast.git
cd weather-forecast

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ (Optional) Run the Streamlit app
streamlit run app.py
```

---

## 👩‍💻 Author
**Cemre Küçükgöde**  
🌐 [Portfolio](https://cemrekucukgode.com)  
💼 [LinkedIn](https://linkedin.com/in/cemre-kucukgode/)  
💻 [GitHub](https://github.com/Cemrekucukg)

---




