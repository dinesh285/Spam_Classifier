# 🛡️ AI SMS GUARD – Intelligent SMS Spam Detection

<p align="center">
  <strong>AI-Powered SMS Spam Detection Using Machine Learning</strong>
</p>

<p align="center">
  🚀 Detect Spam Messages | 🤖 Machine Learning | 🔐 Safer Messaging
</p>

---

## 🌐 Live Application

**Try AI SMS GUARD Online:**

👉 https://spamclassifier-ml0.streamlit.app/

## 📌 Project Overview

AI SMS GUARD is an intelligent SMS spam detection system developed using Machine Learning and Natural Language Processing (NLP). The application automatically identifies whether an SMS message is **SPAM or NOT SPAM**.

The system analyzes the text content of SMS messages and uses a trained machine learning model to classify messages into spam and legitimate categories.

The project uses the UCI SMS Spam Collection dataset and applies TF-IDF (Term Frequency-Inverse Document Frequency) for feature extraction and the Multinomial Naïve Bayes algorithm for classification.

The application is developed using Streamlit, providing a simple and interactive web interface where users can enter messages and instantly view prediction results.

## 🎯 Project Objectives

- Develop an automated SMS spam detection system.
- Identify unwanted and suspicious SMS messages.
- Apply Machine Learning techniques to text classification.
- Convert text messages into numerical features using TF-IDF.
- Implement Multinomial Naïve Bayes for classification.
- Provide an interactive and user-friendly web application.
- Deploy the application online using Streamlit Community Cloud.

## ✨ Key Features

- 📩 **SMS Classification:** Identifies SPAM and NOT SPAM messages.
- 🤖 **Machine Learning:** Uses Multinomial Naïve Bayes.
- 🔍 **Text Analysis:** Processes SMS messages using TF-IDF.
- 📊 **Dataset Analytics:** Displays message statistics and distribution.
- ⚡ **Instant Prediction:** Provides quick classification results.
- 📈 **Confidence Score:** Displays the model's prediction confidence.
- 🌐 **Online Access:** Available through Streamlit Community Cloud.
- 🎨 **Interactive Interface:** Simple and user-friendly dashboard.

## 📂 Dataset Information

**Dataset Name:** UCI SMS Spam Collection

**Dataset Source:** UCI Machine Learning Repository

The dataset contains 5,572 SMS messages divided into two categories.

| Dataset Details | Count |
|---|---:|
| Total Messages | 5,572 |
| Spam Messages | 747 |
| Ham Messages | 4,825 |
| Training Data (80%) | 4,457 |
| Testing Data (20%) | 1,115 |

**Categories:**

- `spam` – Unwanted or promotional SMS messages.
- `ham` – Normal and legitimate SMS messages.

## 🧠 Machine Learning Algorithm

### Multinomial Naïve Bayes (MNB)

The project uses the Multinomial Naïve Bayes algorithm, a supervised machine learning classification technique based on Bayes' Theorem.

It calculates the probability of a message belonging to the spam or legitimate category using the extracted text features.

**Why Multinomial Naïve Bayes?**

- Suitable for text classification.
- Works with TF-IDF features.
- Fast training and prediction.
- Computationally efficient.
- Easy to implement.

### Feature Extraction – TF-IDF

TF-IDF converts SMS text into numerical feature vectors. It identifies the importance of words within individual messages compared with the complete dataset.

These numerical features are provided to the Multinomial Naïve Bayes classifier for training and prediction.

## ⚙️ Project Workflow

```text
        SMS SPAM DATASET
                |
                v
        DATA PREPROCESSING
                |
                v
         TRAIN-TEST SPLIT
              80:20
                |
                v
        TF-IDF VECTORIZATION
                |
                v
       MULTINOMIAL NAIVE BAYES
                |
                v
          MODEL TRAINING
                |
                v
           MODEL TESTING
                |
                v
          SMS PREDICTION
                |
                v
         FINAL CLASSIFICATION
                |
          +-----+-----+
          |           |
          v           v
         SPAM      NOT SPAM
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data handling |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| TF-IDF | Feature extraction |
| Multinomial Naïve Bayes | Classification |
| Joblib | Model saving and loading |
| Streamlit | Web application |
| GitHub | Source code management |
| Streamlit Cloud | Application deployment |

## 🖥️ Application Working

1. Open the AI SMS GUARD web application.
2. Enter an SMS message in the input area.
3. Click the Analyze Message button.
4. The message is converted into numerical features using TF-IDF.
5. The trained Multinomial Naïve Bayes model analyzes the message.
6. The application displays the prediction as SPAM or NOT SPAM.
7. The corresponding confidence score is displayed.

## 📦 Installation and Setup

Follow these steps to run the project locally.

**Step 1: Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2: Open the project folder**

```bash
cd AI-SMS-GUARD
```

**Step 3: Install the required libraries**

```bash
pip install -r requirements.txt
```

**Step 4: Run the Streamlit application**

```bash
streamlit run app.py
```

**Step 5: Open in browser**

```text
http://localhost:8501
```

Make sure the trained model, TF-IDF vectorizer, and other required project files are available in their expected locations.

## 📁 Project Structure

An example project structure:

```text
AI-SMS-GUARD/
│
├── app.py
├── requirements.txt
├── model.pkl
├── vectorizer.pkl
├── spam.csv
│
├── README.md
└── .gitignore
```

*Note: Adjust the filenames and folder structure to match the actual files in your repository.*

## 🔮 Future Enhancements

- Multilingual SMS spam detection.
- Suspicious URL identification.
- Advanced Deep Learning algorithms.
- Real-time SMS monitoring.
- Mobile application integration.
- Improved spam detection using larger datasets.

## 🎯 Project Outcome

AI SMS GUARD demonstrates how Machine Learning and Natural Language Processing can be used to solve real-world communication security problems.

The project provides an interactive platform for identifying spam and legitimate SMS messages through an online web application.

## 🌐 Deployment

**Application Name:** AI SMS GUARD

**Platform:** Streamlit Community Cloud

**Live Application:** https://spamclassifier-ml0.streamlit.app/

## 📚 References

1. UCI Machine Learning Repository – SMS Spam Collection Dataset: https://archive.ics.uci.edu/dataset/228/sms+spam+collection
2. Scikit-learn Documentation: https://scikit-learn.org/
3. Streamlit Documentation: https://docs.streamlit.io/
4. Python Documentation: https://docs.python.org/
5. Pandas Documentation: https://pandas.pydata.org/docs/

---

<p align="center">
  <strong>🛡️ AI SMS GUARD</strong>
  <br/>
  Intelligent SMS Spam Detection Using Machine Learning
  <br/><br/>
  🚀 Making Digital Communication Safer with AI
</p>
