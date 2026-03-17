from unittest.mock import patch, MagicMock
from src.infrastructure.adapters.outgoing.sentiment_analysis_adapter import SentimentAnalysisAdapter

@patch('src.infrastructure.adapters.outgoing.sentiment_analysis_adapter.mlflow.pyfunc.load_model')
def test_sentiment_analysis_adapter_predict(mock_load_model):
    mock_model_instance = MagicMock()
    mock_model_instance.predict.return_value = [0.75] 
    mock_load_model.return_value = mock_model_instance

    adapter = SentimentAnalysisAdapter(model_path="fake/path")

    score = adapter.predict("Test sentence")

    mock_model_instance.predict.assert_called_once_with(["Test sentence"])
    assert score == 0.75
    assert isinstance(score, float)