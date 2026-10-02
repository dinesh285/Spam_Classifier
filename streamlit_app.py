import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="AI Spam Classifier",
    page_icon="📩",
    layout="wide"
)

# Load model and vectorizer
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# Load dataset
df = pd.read_csv("dataset/spam.csv")

# Statistics
total_messages = len(df)
spam_messages = (df["label"] == "spam").sum()
ham_messages = (df["label"] == "ham").sum()

# Title
st.title("📩 AI Spam Classifier")
st.subheader("SMS Spam Detection using Machine Learning")

st.write(
    "This application uses TF-IDF and Multinomial Naïve Bayes "
    "to classify SMS messages as Spam or Not Spam."
)

st.divider()

# Statistics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💬 Total Messages", total_messages)

with col2:
    st.metric("🚨 Spam Messages", spam_messages)

with col3:
    st.metric("✅ Not Spam", ham_messages)

st.divider()

# Message input
st.header("🔍 Check Your Message")

message = st.text_area(
    "Enter your SMS message:",
    placeholder="Example: Congratulations! You have won a free prize..."
)

# Prediction button
if st.button("🚀 Check Message", use_container_width=True):

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:
        # Convert message to TF-IDF
        message_tfidf = vectorizer.transform([message])

        # Prediction
        prediction = model.predict(message_tfidf)[0]

        if prediction == 1:
            st.error("🚨 SPAM MESSAGE")
            st.write("This message has been classified as **Spam**.")

        else:
            st.success("✅ NOT SPAM")
            st.write("This message appears to be legitimate.")

st.divider()

# How it works
st.header("⚙️ How It Works")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### 1️⃣ Input")
    st.write("Enter an SMS message.")

with col2:
    st.markdown("### 2️⃣ TF-IDF")
    st.write("Convert text into numerical features.")

with col3:
    st.markdown("### 3️⃣ Naïve Bayes")
    st.write("The trained ML model analyzes the message.")

with col4:
    st.markdown("### 4️⃣ Prediction")
    st.write("Display Spam or Not Spam.")

st.divider()

st.caption("Machine Learning • NLP • TF-IDF • Multinomial Naïve Bayes")