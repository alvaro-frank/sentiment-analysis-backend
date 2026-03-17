from pydantic import BaseModel

class SentimentResponse(BaseModel):
    text: str
    sentiment_score: float
    label: str