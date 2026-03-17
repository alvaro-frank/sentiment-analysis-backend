from src.application.ports.ports import SentimentModelPort
from src.domain.entities import SentimentLabel
from src.application.dtos.dtos import SentimentInputDTO, SentimentOutputDTO

class AnalyzeSentimentUseCase:
    def __init__(self, model_port: SentimentModelPort):
        self.model_port = model_port

    def execute(self, input_dto: SentimentInputDTO) -> SentimentOutputDTO:
        score = self.model_port.predict(input_dto.text)

        if score >= 0.3:
            label = SentimentLabel.POSITIVE
        elif score <= -0.3:
            label = SentimentLabel.NEGATIVE
        else:
            label = SentimentLabel.NEUTRAL

        return SentimentOutputDTO(
            text=input_dto.text,
            sentiment_score=round(score, 4),
            label=label
        )