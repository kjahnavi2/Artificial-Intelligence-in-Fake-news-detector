import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

st.title("📰 Fake News Detector")
st.write("Enter a news article below and check if it's **Real** or **Fake**.")

# Load model and vectorizer if already trained
try:
    model = pickle.load(open("src/model.pkl", "rb"))
    vectorizer = pickle.load(open("src/vectorizer.pkl", "rb"))
    st.success("Model loaded successfully!")
except:
    st.warning("Train the model first using the notebook and save it in src/.")

# User input
user_input = st.text_area("Paste News Article")

if st.button("Predict"):
    if user_input.strip() == "":
        st.error("Please enter some text.")
    else:
        X_input = vectorizer.transform([user_input])
        prediction = model.predict(X_input)[0]
        result = "✅ Real News" if prediction == 0 else "❌ Fake News"
        st.subheader(result)
