import pytest
from src.application.ports.ports import SentimentModelPort
from src.application.dtos.dtos import SentimentInputDTO
from src.domain.entities import SentimentLabel
from src.application.use_cases.analyse_sentiment_use_case import AnalyzeSentimentUseCase

class MockModelAdapter(SentimentModelPort):
    """Um mock perfeito que finge ser o modelo de MLflow."""
    def __init__(self, mock_score: float):
        self.mock_score = mock_score

    def predict(self, text: str) -> float:
        return self.mock_score

def test_analyze_sentiment_positive():
    mock_port = MockModelAdapter(mock_score=0.85)
    use_case = AnalyzeSentimentUseCase(model_port=mock_port)
    input_dto = SentimentInputDTO(text="The market is doing great!")

    result = use_case.execute(input_dto)

    assert result.sentiment_score == 0.85
    assert result.label == SentimentLabel.POSITIVE
    assert result.text == "The market is doing great!"

def test_analyze_sentiment_negative():
    mock_port = MockModelAdapter(mock_score=-0.4)
    use_case = AnalyzeSentimentUseCase(model_port=mock_port)
    
    result = use_case.execute(SentimentInputDTO(text="Revenue dropped."))
    
    assert result.label == SentimentLabel.NEGATIVE

def test_analyze_sentiment_neutral():
    mock_port = MockModelAdapter(mock_score=0.1)
    use_case = AnalyzeSentimentUseCase(model_port=mock_port)
    
    result = use_case.execute(SentimentInputDTO(text="The market is stable."))
    
    assert result.label == SentimentLabel.NEUTRAL