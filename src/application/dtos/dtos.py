from dataclasses import dataclass
from src.domain.entities import SentimentLabel

@dataclass(frozen=True)
class SentimentInputDTO:
    text: str

@dataclass(frozen=True)
class SentimentOutputDTO:
    text: str
    sentiment_score: float
    label: SentimentLabel