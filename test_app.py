
from app import app

def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Sentiment Analysis API is running"

def test_positive_sentiment():
    client = app.test_client()
    response = client.post(
        "/predict",
        json={"text": "I love this product, it is amazing!"})
    assert response.status_code == 200
    assert response.get_json()["sentiment"] == "Positive"

def test_negative_sentiment():
    client = app.test_client()
    response = client.post(
        "/predict",
        json={"text": "I hate this, it is terrible!"})
    assert response.status_code == 200
    assert response.get_json()["sentiment"] == "Negative"

def test_missing_text():
    client = app.test_client()
    response = client.post("/predict", json={})
    assert response.status_code == 400
