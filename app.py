import streamlit as st
import pickle
import numpy as np
import joblib
# Load all components
st.set_page_config(page_title="Tweet Emotion Classifier", layout="centered")
@st.cache_resource
def load_all():
    model = joblib.load("best_svm_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    label_encoder = joblib.load("label_encoder.pkl")
    return model, vectorizer, label_encoder


model, vectorizer, label_encoder = load_all()

# Streamlit UI
st.title("🔍 Tweet Emotion Classifier")
st.write("Enter a tweet below and get the predicted emotion using an SVM model.")

tweet = st.text_area("📨 Your Tweet", "")

if st.button("🔎 Classify Emotion"):
    if tweet.strip() == "":
        st.warning("Please enter a tweet.")
    else:
        # Vectorize and predict
        X_input = vectorizer.transform([tweet])
        prediction = model.predict(X_input)
        emotion_label = label_encoder.inverse_transform(prediction)[0]
        st.success(f"🎭 Predicted Emotion: **{emotion_label}**")
