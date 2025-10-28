import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# Load model & preprocessors once
@st.cache_resource
def load_all():
    with open("wine_scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    with open("wine_powertransform.pkl", "rb") as f:
        pt = pickle.load(f)
    model = load_model("wine_mlp_model.h5")
    return scaler, pt, model

scaler, pt, model = load_all()

feature_names = [
    "fixed acidity", "volatile acidity", "citric acid", "residual sugar",
    "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density",
    "pH", "sulphates", "alcohol"
]

st.title("Wine Quality Predictor")

st.write(
    "Enter feature values for a **red wine** sample. All features must be entered. "
    "Prediction is based on a neural network classifier trained on the UCI wine quality dataset."
)

# Simple input form for all features
with st.form("input_form"):
    inputs = []
    for feat in feature_names:
        val = st.number_input(f"{feat}", value=0.0, format="%.3f")
        inputs.append(val)
    submitted = st.form_submit_button("Predict Quality")

if submitted:
    x_df = pd.DataFrame([inputs], columns=feature_names)
    x_trans = pt.transform(x_df)
    x_scaled = scaler.transform(x_trans)
    pred_probs = model.predict(x_scaled)
    pred_class = int(np.argmax(pred_probs, axis=1)[0]) + 3
    st.success(f"Predicted Wine Quality: {pred_class}")

st.caption(
    "Upload your trained model (wine_mlp_model.h5), scaler (wine_scaler.pkl),"
    " and transformer (wine_powertransform.pkl) with this file when deploying."
)
