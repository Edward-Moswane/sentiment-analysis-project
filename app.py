from flask import Flask, request, jsonify
import joblib
import re

app = Flask(__name__)

# Load the trained sentiment model
model = joblib.load("sentiment_model.pkl")

def clean_tweet(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\.\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Sentiment Analysis API is running"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if not data or not isinstance(data.get("text"), str):
        return jsonify({
            "error": "Please provide text as a string"
        }), 400

    text = clean_tweet(data["text"])

    if not text:
        return jsonify({
            "error": "Text cannot be empty"
        }), 400

    prediction = int(model.predict([text])[0])
    probabilities = model.predict_proba([text])[0]

    sentiment = "Positive" if prediction == 1 else "Negative"

    return jsonify({
        "text": data["text"],
        "sentiment": sentiment,
        "prediction": prediction,
        "confidence": round(float(max(probabilities)), 4)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
