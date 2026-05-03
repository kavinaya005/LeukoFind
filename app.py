# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 19:19:58 2025

@author: kavin
"""


import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input
import os
import base64

# -------------------------------
# Theme / Colors
# -------------------------------
PRIMARY_COLOR = "#4A90E2"  # Main button / highlight
SUCCESS_COLOR = "#34D399"  # Benign / success
ERROR_COLOR = "#F87171"    # Cancerous / error
INFO_COLOR = "#808080"     # Info / subtitle
BG_COLOR = "#FFFFFF"       # Default background (will be overridden)

# -------------------------------
# Path to trained model and local dataset
# -------------------------------
MODEL_PATH = "D:/Projects/Leukemia project/ResNet50_best.keras"
DATASET_PATH = r"D:/archive1/Blood cell Cancer [ALL]"  # adjust your path

# -------------------------------
# Path to background image
# -------------------------------
BACKGROUND_IMAGE_PATH = "D:/Projects/Leukemia project/background 1.jpg"

# -------------------------------
# Load and encode background image
# -------------------------------

with open(BACKGROUND_IMAGE_PATH, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Streamlit CSS and Fonts with Background
st.markdown(f"""
<link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{encoded_string}");
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
}}
.stButton>button {{
    background-color: {PRIMARY_COLOR} !important;
    color: white !important;
    font-family: 'Open Sans', sans-serif !important;
    font-weight: 400 !important;
}}
.stButton>button:hover {{
    background-color: #357ABD !important;
}}
p, div, span {{
    font-family: 'Open Sans', sans-serif !important;
    font-weight: 400 !important;
}}
p {{
    font-size:16px !important;
    line-height:1.6 !important;
    text-align: justify !important;
}}
</style>
""", unsafe_allow_html=True)
#-------------------------------
# Load ResNet50 Keras Model
# -------------------------------
@st.cache_resource
def load_model_keras(path=MODEL_PATH):
    model = tf.keras.models.load_model(path)
    return model

model = load_model_keras()

# -------------------------------
# Determine class order from local dataset
# -------------------------------
classes = sorted([c for c in os.listdir(DATASET_PATH) if os.path.isdir(os.path.join(DATASET_PATH, c))])

# -------------------------------
# Image Preprocessing Function
# -------------------------------
def preprocess_image(image, target_size=(224,224)):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

# -------------------------------
# Prediction Function
# -------------------------------
def predict_actual(uploaded_file):
    image = Image.open(uploaded_file)
    img_array = preprocess_image(image)
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions, axis=1)[0]
    confidence = predictions[0][predicted_index]
    return classes[predicted_index], confidence

# -------------------------------
# HOME CONTENT
# -------------------------------
st.markdown(f"<h1 style='color:{PRIMARY_COLOR};'>LeukoFind 🔍🔬</h1>", unsafe_allow_html=True)
st.markdown(f"<h4 style='color:{INFO_COLOR};'>Deep Learning-Based Detection of B-Cell Acute Lymphoblastic Leukemia from Blood smear images</h4>", unsafe_allow_html=True)

st.markdown(
f"""
<div style="
    text-align: justify; 
    font-size:16px; 
    line-height:1.6; 
    font-weight:400;
    max-width:900px;
    margin-left:auto;
    margin-right:auto;">
    Leukemia is a type of blood cancer characterized by the abnormal and uncontrolled growth of white blood cells, which can interfere with the body’s ability to fight infections and perform normal blood functions. B-cell Acute Lymphoblastic Leukemia (B-ALL) is a specific form of leukemia where immature B-lymphocytes proliferate uncontrollably in the bone marrow and bloodstream. The disease can be classified into several subtypes: Pro-B, Early Pre-B and 
    Pre-B. Benign indicates hematogones, non-cancerous cells. Early detection and accurate classification are crucial for proper treatment and effective patient care.
    <br><br>
    <span style="color:{PRIMARY_COLOR}; font-weight:1000;">LeukoFind 🔍🔬 </span> helps you predict B-cell ALL from "Blood smear images" — Click <em>Analyze</em> to start 
    and view the prediction results!
</div>
""", unsafe_allow_html=True
)

# Analyze button
if st.button("Analyze", key="analyze_btn"):
    st.session_state['show_prediction'] = True

# -------------------------------
# PREDICTION SECTION
# -------------------------------
if st.session_state.get('show_prediction', False):
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='color:{PRIMARY_COLOR};'>Prediction</h1>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload Blood Smear Image", type=["jpg","jpeg","png"])
    
    if uploaded_file is not None:
        
        st.image(uploaded_file, caption="Uploaded Blood Smear Image", width=200, use_container_width=False)
        
        if st.button("Predict"):
            result, confidence = predict_actual(uploaded_file)
            confidence_percent = confidence * 100
            if result.lower() == "benign":
                st.success(f"Result: {result} (Non-Cancerous) | Confidence: {confidence_percent:.2f}%")
                st.info("The blood smear shows no signs of leukemia, but further medical evaluation is recommended to confirm overall health.")
            else:
                if "pro-b" in result.lower():
                    st.error(f"Result: {result} (Cancerous) | Confidence: {confidence_percent:.2f}%")
                    st.warning("Pro-B detected. Highly immature cancerous cells. Immediate medical attention recommended.")
                elif "early pre-b" in result.lower():
                    st.error(f"Result: {result} (Cancerous) | Confidence: {confidence_percent:.2f}%")
                    st.warning("Early Pre-B detected. Cancerous cells present in early development. Consult a medical professional soon.")
                elif "pre-b" in result.lower():
                    st.error(f"Result: {result} (Cancerous) | Confidence: {confidence_percent:.2f}%")
                    st.warning("Pre-B detected. Cancerous cells present. Seek consultation with a doctor.")
