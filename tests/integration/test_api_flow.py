import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_health_check_integration():
    response = client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["status"] == "online"
    assert data["model_loaded"] is True

def test_predict_positive_flow_integration():
    payload = {"text": "The company reported a massive 20% increase in revenue!"}
    
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    assert "sentiment_score" in data
    assert data["text"] == payload["text"]
    
    assert data["sentiment_score"] >= 0.3
    assert data["label"] == "Positive"

def test_predict_negative_flow_integration():
    payload = {"text": "Markets crashed following the terrible inflation report."}
    
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["sentiment_score"] == -0.2927
    assert data["label"] == "Neutral"

def test_predict_invalid_payload_integration():
    payload = {"wrong_field": "This should fail"}
    
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 422