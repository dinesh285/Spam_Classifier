import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="AI SMS Guard",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- SIMPLE DESIGN ----------------

st.markdown("""
<style>

.stApp {
    background: #07111f;
    color: white;
}

h1 {
    color: #00c8ff;
    font-size: 42px !important;
}

h2, h3 {
    color: white;
}

.subtitle {
    color: #9fb3c8;
    font-size: 18px;
}

.card {
    background: #0d1b2a;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #183b56;
    text-align: center;
}

.big-number {
    font-size: 32px;
    font-weight: bold;
    color: #00c8ff;
}

.small-text {
    color: #9fb3c8;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------

model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# ---------------- LOAD DATA ----------------

df = pd.read_csv("dataset/spam.csv")

total = len(df)
spam = int((df["label"] == "spam").sum())
not_spam = int((df["label"] == "ham").sum())

spam_percentage = spam / total * 100
safe_percentage = not_spam / total * 100

# ---------------- HEADER ----------------

st.title("🛡️ AI SMS GUARD")

st.markdown(
    '<p class="subtitle">Intelligent SMS Threat Detection using Machine Learning</p>',
    unsafe_allow_html=True
)

st.caption("TF-IDF  •  Multinomial Naïve Bayes  •  Natural Language Processing")

st.divider()

# ---------------- STATISTICS ----------------

st.subheader("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📩 Total Messages", f"{total:,}")

with col2:
    st.metric("🚨 Spam Messages", f"{spam:,}")

with col3:
    st.metric("✅ Not Spam", f"{not_spam:,}")

st.divider()

# ---------------- SPAM CHECKER ----------------

st.subheader("🔍 Check Your SMS")

st.write(
    "Enter an SMS message below and our machine learning model "
    "will determine whether it is spam or not spam."
)

message = st.text_area(
    "SMS Message",
    placeholder="Example: Congratulations! You have won a free prize...",
    height=140
)

if st.button("🔎 Analyze Message", use_container_width=True):

    if message.strip() == "":
        st.warning("Please enter a message first.")

    else:

        # Convert message to TF-IDF
        message_tfidf = vectorizer.transform([message])

        # Prediction
        prediction = model.predict(message_tfidf)[0]

        # Probability
        probability = model.predict_proba(message_tfidf)[0]

        if prediction == 1:

            confidence = probability[1] * 100

            st.error("🚨 SPAM MESSAGE")

            st.write(
                f"This message has been classified as **SPAM**."
            )

            st.progress(int(confidence))

            st.caption(
                f"Model confidence: {confidence:.1f}%"
            )

        else:

            confidence = probability[0] * 100

            st.success("✅ NOT SPAM")

            st.write(
                "This message appears to be a legitimate message."
            )

            st.progress(int(confidence))

            st.caption(
                f"Model confidence: {confidence:.1f}%"
            )

st.divider()

# ---------------- DATASET CHART ----------------

st.subheader("📈 Message Distribution")

chart = pd.DataFrame(
    {
        "Category": ["Spam", "Not Spam"],
        "Messages": [spam, not_spam]
    }
)

st.bar_chart(
    chart.set_index("Category")
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "🚨 Spam Percentage",
        f"{spam_percentage:.2f}%"
    )

with col2:
    st.metric(
        "✅ Not Spam Percentage",
        f"{safe_percentage:.2f}%"
    )

st.divider()

# ---------------- HOW IT WORKS ----------------

st.subheader("⚙️ How It Works")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("### 1️⃣")
    st.write("**SMS Input**")
    st.caption("User enters an SMS message.")

with col2:
    st.write("### 2️⃣")
    st.write("**TF-IDF**")
    st.caption("Text is converted into numerical features.")

with col3:
    st.write("### 3️⃣")
    st.write("**Naïve Bayes**")
    st.caption("The trained ML model analyzes the message.")

with col4:
    st.write("### 4️⃣")
    st.write("**Prediction**")
    st.caption("Spam or Not Spam is displayed.")

st.divider()

# ---------------- FOOTER ----------------

st.caption(
    "🛡️ AI SMS GUARD  |  Machine Learning • NLP • TF-IDF • Naïve Bayes"
)
