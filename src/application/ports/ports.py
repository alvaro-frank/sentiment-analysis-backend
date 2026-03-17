from abc import ABC, abstractmethod

class SentimentModelPort(ABC):
    @abstractmethod
    def predict(self, text: str) -> float:
        pass