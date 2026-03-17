from fastapi import APIRouter, HTTPException, Request
from src.infrastructure.schemas.request import SentimentRequest
from src.infrastructure.schemas.response import SentimentResponse
from src.application.dtos.dtos import SentimentInputDTO
from src.application.use_cases.analyse_sentiment_use_case import AnalyzeSentimentUseCase

sentiment_router = APIRouter()

@sentiment_router.post("/predict", response_model=SentimentResponse)
def predict_sentiment(payload: SentimentRequest, request: Request):
    use_case: AnalyzeSentimentUseCase = request.app.state.analyze_sentiment_use_case
    
    try:
        app_input_dto = SentimentInputDTO(text=payload.text)
        
        app_output_dto = use_case.execute(app_input_dto)
        
        return SentimentResponse(
            text=app_output_dto.text,
            sentiment_score=app_output_dto.sentiment_score,
            label=app_output_dto.label.value
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))