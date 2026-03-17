from enum import Enum
from dataclasses import dataclass

class SentimentLabel(str, Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"

@dataclass
class SentimentResult:
    text: str
    score: float
    label: SentimentLabel