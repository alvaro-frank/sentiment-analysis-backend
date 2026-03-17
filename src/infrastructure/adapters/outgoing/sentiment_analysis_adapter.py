import mlflow.pyfunc
from src.application.ports.ports import SentimentModelPort

class SentimentAnalysisAdapter(SentimentModelPort):
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self):
        try:
            return mlflow.pyfunc.load_model(self.model_path)
        except Exception as e:
            print(f"!!! Error loading model: {e}")
            raise RuntimeError("Model cannot be initialized.") from e

    def predict(self, text: str) -> float:
        if self.model is None:
            raise RuntimeError("Model unavailable for prediction.")
        
        score_array = self.model.predict([text])
        return float(score_array[0])