# Sentiment Analysis Project

##Project Overview

This project implements an end-to-end sentiment analysis system that classifies tweets as positive or negative. It uses the Sentiment140 dataset, a Logistic Regression model, a Flask API, Docker containerization, and GitHub Actions for automated testing and image publishing.

##Dataset and Preprocessing

The Sentiment140 dataset contains 1.6 million tweets with sentiment labels. A sample of approximately 200,000 records was selected and balanced between the two sentiment classes.

Preprocessing included cleaning tweet text and preparing the data for model training.

##Model Training and Evaluation

A Logistic Regression classifier was trained to predict tweet sentiment.

test results:
- Accuracy: 80.16%
- Negative-class F1-score: 0.80
- Positive-class F1-score: 0.80

## Flask Prediction API

The Flask application exposes the following endpoints:

- `GET /` — checks whether the API is running.
- `POST /predict` — accepts tweet text and returns the predicted sentiment and confidence.

Example request:

```json
{"text": "I love this product!"}
```

Example response:

```json
{"confidence": 0.9727,
  "prediction": 1,
  "sentiment": "Positive",
  "text": "I love this product!"}
```

## 5. Automated Testing and CI/CD

GitHub Actions runs automated tests, builds the Docker image, and publishes images to Docker Hub when changes are pushed to the `main` branch.

The repository includes `test_app.py` for API testing and `.github/workflows/ci.yml` for the CI workflow.

## 6. Docker Deployment

Docker Hub repository:

https://hub.docker.com/r/edwardmoswane/sentiment-analysis-project

Pull the image:

```bash
docker pull edwardmoswane/sentiment-analysis-project:latest
```

Run the application:

```bash
docker run --rm -p 5000:5000 edwardmoswane/sentiment-analysis-project:latest
```

Open `http://localhost:5000/` to check the API.

## Versioning and Rollback

Docker images are tagged with `latest` and Git commit identifiers. These tags help identify versions and select an earlier image if a rollback is required.

See `VERSIONING_AND_ROLLBACK.md` for the rollback procedure.

##Project Files

- `app.py` — Flask API application.
- `sentiment_model.pkl` — trained model.
- `requirements.txt` — Python dependencies.
- `Dockerfile` — Docker image configuration.
- `test_app.py` — automated API tests.
- `.github/workflows/ci.yml` — GitHub Actions workflow.
- `VERSIONING_AND_ROLLBACK.md` — versioning and rollback documentation.
