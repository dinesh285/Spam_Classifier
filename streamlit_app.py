import streamlit as st
import pandas as pd
import joblib

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI SMS GUARD",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* ---------- MAIN BACKGROUND ---------- */

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(0, 180, 255, 0.12), transparent 30%),
            radial-gradient(circle at 90% 20%, rgba(0, 100, 255, 0.10), transparent 30%),
            linear-gradient(135deg, #050914 0%, #08111f 50%, #050914 100%);
        color: #ffffff;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ---------- HEADER ---------- */

    .hero {
        padding: 30px;
        border-radius: 24px;
        border: 1px solid rgba(0, 200, 255, 0.25);
        background: linear-gradient(
            135deg,
            rgba(7, 25, 45, 0.95),
            rgba(5, 14, 28, 0.90)
        );
        box-shadow:
            0 0 40px rgba(0, 150, 255, 0.10),
            inset 0 0 30px rgba(0, 150, 255, 0.03);
        margin-bottom: 25px;
    }

    .brand {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: 1px;
        background: linear-gradient(90deg, #00d9ff, #4c8dff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        color: #a8bfd8;
        font-size: 18px;
        margin-top: 5px;
    }

    .tech {
        color: #6fdcff;
        font-size: 14px;
        margin-top: 12px;
        letter-spacing: 1px;
    }

    .online {
        background: rgba(0, 220, 130, 0.10);
        border: 1px solid rgba(0, 255, 150, 0.30);
        color: #35e99a;
        border-radius: 20px;
        padding: 8px 16px;
        display: inline-block;
        font-size: 13px;
        font-weight: 600;
    }

    /* ---------- STAT CARDS ---------- */

    .stat-card {
        background: linear-gradient(
            145deg,
            rgba(12, 30, 52, 0.95),
            rgba(6, 18, 34, 0.95)
        );
        border: 1px solid rgba(70, 170, 255, 0.20);
        border-radius: 20px;
        padding: 22px;
        text-align: center;
        min-height: 140px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.20);
    }

    .stat-icon {
        font-size: 25px;
    }

    .stat-number {
        font-size: 35px;
        font-weight: 800;
        color: #ffffff;
        margin-top: 5px;
    }

    .stat-label {
        color: #91aac2;
        font-size: 14px;
    }

    /* ---------- SECTION TITLE ---------- */

    .section-title {
        text-align: center;
        font-size: 30px;
        font-weight: 750;
        color: #ffffff;
        margin-top: 35px;
        margin-bottom: 8px;
    }

    .section-description {
        text-align: center;
        color: #8fa8c0;
        margin-bottom: 25px;
    }

    /* ---------- SCANNER ---------- */

    .scanner {
        background: linear-gradient(
            145deg,
            rgba(10, 29, 50, 0.98),
            rgba(5, 17, 31, 0.98)
        );
        border: 1px solid rgba(0, 200, 255, 0.22);
        border-radius: 24px;
        padding: 30px;
        box-shadow: 0 15px 45px rgba(0,0,0,0.30);
    }

    /* ---------- TEXT AREA ---------- */

    textarea {
        background-color: #071321 !important;
        color: #ffffff !important;
        border: 1px solid #164b70 !important;
        border-radius: 15px !important;
    }

    textarea:focus {
        border: 1px solid #00c8ff !important;
        box-shadow: 0 0 15px rgba(0, 200, 255, 0.15) !important;
    }

    /* ---------- BUTTON ---------- */

    .stButton > button {
        width: 100%;
        border-radius: 14px;
        border: 1px solid rgba(0, 210, 255, 0.45);
        background: linear-gradient(90deg, #0077ff, #00b8ff);
        color: white;
        font-size: 17px;
        font-weight: 700;
        padding: 14px;
        transition: all 0.25s ease;
        box-shadow: 0 8px 25px rgba(0, 140, 255, 0.20);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 35px rgba(0, 180, 255, 0.35);
    }

    /* ---------- RESULT CARDS ---------- */

    .spam-result {
        margin-top: 25px;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        background: linear-gradient(
            135deg,
            rgba(100, 20, 25, 0.90),
            rgba(45, 10, 15, 0.95)
        );
        border: 1px solid rgba(255, 70, 70, 0.50);
        box-shadow: 0 0 30px rgba(255, 40, 40, 0.12);
    }

    .safe-result {
        margin-top: 25px;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        background: linear-gradient(
            135deg,
            rgba(10, 85, 60, 0.90),
            rgba(5, 45, 35, 0.95)
        );
        border: 1px solid rgba(50, 255, 160, 0.40);
        box-shadow: 0 0 30px rgba(20, 255, 150, 0.10);
    }

    .result-icon {
        font-size: 50px;
    }

    .result-title {
        font-size: 28px;
        font-weight: 800;
        margin-top: 8px;
    }

    .result-text {
        color: #c0d0df;
        font-size: 15px;
    }

    /* ---------- WORKFLOW ---------- */

    .workflow-card {
        background: rgba(8, 24, 42, 0.90);
        border: 1px solid rgba(80, 170, 255, 0.18);
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        min-height: 180px;
    }

    .workflow-icon {
        font-size: 35px;
        margin-bottom: 10px;
    }

    .workflow-title {
        color: #ffffff;
        font-size: 18px;
        font-weight: 700;
    }

    .workflow-text {
        color: #91aac2;
        font-size: 13px;
    }

    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #6f879e;
        font-size: 13px;
        padding-top: 40px;
        line-height: 1.8;
    }

</style>
""", unsafe_allow_html=True)

# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    model = joblib.load("model/spam_model.pkl")
    vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

    return model, vectorizer


model, vectorizer = load_model()

# ============================================================
# LOAD DATASET
# ============================================================

@st.cache_data
def load_dataset():

    return pd.read_csv("dataset/spam.csv")


df = load_dataset()

# Dataset statistics
total_messages = len(df)
spam_messages = int((df["label"] == "spam").sum())
ham_messages = int((df["label"] == "ham").sum())

spam_percentage = (spam_messages / total_messages) * 100
ham_percentage = (ham_messages / total_messages) * 100

# ============================================================
# HERO HEADER
# ============================================================

st.markdown("""
<div class="hero">

    <div style="display:flex; justify-content:space-between;
                align-items:center; gap:20px; flex-wrap:wrap;">

        <div>

            <div class="brand">
                🛡️ AI SMS GUARD
            </div>

            <div class="subtitle">
                Intelligent SMS Threat Detection
            </div>

            <div class="tech">
                TF-IDF &nbsp; • &nbsp;
                Multinomial Naïve Bayes &nbsp; • &nbsp;
                Machine Learning
            </div>

        </div>

        <div class="online">
            ● SYSTEM ONLINE
        </div>

    </div>

</div>
""", unsafe_allow_html=True)

# ============================================================
# STATISTICS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="stat-card">

        <div class="stat-icon">📩</div>

        <div class="stat-number">
            {total_messages:,}
        </div>

        <div class="stat-label">
            TOTAL MESSAGES
        </div>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-card">

        <div class="stat-icon">🚨</div>

        <div class="stat-number">
            {spam_messages:,}
        </div>

        <div class="stat-label">
            SPAM MESSAGES
        </div>

    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="stat-card">

        <div class="stat-icon">✅</div>

        <div class="stat-number">
            {ham_messages:,}
        </div>

        <div class="stat-label">
            SAFE MESSAGES
        </div>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# MESSAGE SCANNER
# ============================================================

st.markdown("""
<div class="section-title">
    🔍 MESSAGE SECURITY SCANNER
</div>

<div class="section-description">
    Paste or type an SMS message below and let AI analyze it.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="scanner">', unsafe_allow_html=True)

message = st.text_area(
    "SMS MESSAGE",
    placeholder="Example: Congratulations! You have won a free prize. Click here to claim...",
    height=170,
    label_visibility="collapsed"
)

analyze = st.button(
    "🔍  ANALYZE MESSAGE"
)

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# PREDICTION
# ============================================================

if analyze:

    if not message.strip():

        st.warning("⚠️ Please enter an SMS message to analyze.")

    else:

        message_tfidf = vectorizer.transform([message])

        prediction = model.predict(message_tfidf)[0]

        probability = model.predict_proba(message_tfidf)[0]

        if prediction == 1:

            confidence = probability[1] * 100

            st.markdown(f"""
            <div class="spam-result">

                <div class="result-icon">
                    🚨
                </div>

                <div class="result-title">
                    SPAM DETECTED
                </div>

                <div class="result-text">
                    This message has been classified as suspicious
                    by the AI model.
                </div>

                <br>

                <b>AI Confidence: {confidence:.1f}%</b>

            </div>
            """, unsafe_allow_html=True)

        else:

            confidence = probability[0] * 100

            st.markdown(f"""
            <div class="safe-result">

                <div class="result-icon">
                    🛡️
                </div>

                <div class="result-title">
                    MESSAGE VERIFIED
                </div>

                <div class="result-text">
                    This message has been classified as
                    not spam by the AI model.
                </div>

                <br>

                <b>AI Confidence: {confidence:.1f}%</b>

            </div>
            """, unsafe_allow_html=True)

# ============================================================
# DATASET DISTRIBUTION
# ============================================================

st.markdown("""
<div class="section-title">
    📊 DATASET ANALYTICS
</div>

<div class="section-description">
    Distribution of messages used by the classification system.
</div>
""", unsafe_allow_html=True)

chart_data = pd.DataFrame(
    {
        "Category": ["Spam", "Not Spam"],
        "Messages": [spam_messages, ham_messages]
    }
)

st.bar_chart(
    chart_data.set_index("Category"),
    height=300
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "🚨 Spam Percentage",
        f"{spam_percentage:.2f}%"
    )

with col2:
    st.metric(
        "✅ Safe Percentage",
        f"{ham_percentage:.2f}%"
    )

# ============================================================
# HOW IT WORKS
# ============================================================

st.markdown("""
<div class="section-title">
    ⚙️ HOW AI DETECTS SPAM
</div>

<div class="section-description">
    The complete machine learning pipeline used for classification.
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown("""
    <div class="workflow-card">

        <div class="workflow-icon">
            📩
        </div>

        <div class="workflow-title">
            SMS INPUT
        </div>

        <div class="workflow-text">
            User enters an SMS message for analysis.
        </div>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="workflow-card">

        <div class="workflow-icon">
            🔢
        </div>

        <div class="workflow-title">
            TF-IDF
        </div>

        <div class="workflow-text">
            Text is converted into numerical features.
        </div>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="workflow-card">

        <div class="workflow-icon">
            🧠
        </div>

        <div class="workflow-title">
            NAÏVE BAYES
        </div>

        <div class="workflow-text">
            The trained ML model analyzes the message.
        </div>

    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown("""
    <div class="workflow-card">

        <div class="workflow-icon">
            🛡️
        </div>

        <div class="workflow-title">
            PREDICTION
        </div>

        <div class="workflow-text">
            The system identifies Spam or Not Spam.
        </div>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <b>🛡️ AI SMS GUARD</b><br>

    Intelligent SMS Threat Detection<br>

    Machine Learning • NLP • TF-IDF • Multinomial Naïve Bayes<br>

    <br>

    Built with Python & Streamlit

</div>
""", unsafe_allow_html=True)
