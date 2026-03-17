from fastapi.testclient import TestClient
from fastapi import FastAPI
from src.infrastructure.adapters.ingoing.routers import sentiment_router
from src.application.dtos.dtos import SentimentInputDTO, SentimentOutputDTO
from src.domain.entities import SentimentLabel

app = FastAPI()
app.include_router(sentiment_router)

class MockUseCase:
    def execute(self, input_dto: SentimentInputDTO) -> SentimentOutputDTO:
        return SentimentOutputDTO(
            text=input_dto.text,
            sentiment_score=0.9,
            label=SentimentLabel.POSITIVE
        )

app.state.analyze_sentiment_use_case = MockUseCase()

client = TestClient(app)

def test_predict_endpoint_success():
    payload = {"text": "Company XYZ saw a huge profit margin this year."}
    
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == payload["text"]
    assert data["sentiment_score"] == 0.9
    assert data["label"] == "Positive"

def test_predict_endpoint_validation_error():
    payload = {} 
    
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 422