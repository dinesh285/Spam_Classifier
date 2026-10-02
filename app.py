from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained Machine Learning model
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# Load dataset
df = pd.read_csv("dataset/spam.csv")

# Dataset statistics
total_messages = len(df)
spam_messages = (df["label"] == "spam").sum()
ham_messages = (df["label"] == "ham").sum()


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    message = ""

    if request.method == "POST":

        message = request.form["message"]

        if message.strip():

            # Convert message into TF-IDF
            message_tfidf = vectorizer.transform([message])

            # Predict
            result = model.predict(message_tfidf)[0]

            if result == 1:
                prediction = "SPAM"
            else:
                prediction = "NOT SPAM"

    return render_template(
        "index.html",
        prediction=prediction,
        message=message,
        total_messages=total_messages,
        spam_messages=spam_messages,
        ham_messages=ham_messages
    )


if __name__ == "__main__":
    app.run(debug=True)