FROM python:3.11-slim

WORKDIR /app

COPY app.py .
COPY sentiment_model.pkl .

RUN pip install --no-cache-dir flask scikit-learn joblib

EXPOSE 5000

CMD ["python", "app.py"]
