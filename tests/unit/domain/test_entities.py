from src.domain.entities import SentimentLabel

def test_sentiment_label_values():
    assert SentimentLabel.POSITIVE.value == "Positive"
    assert SentimentLabel.NEGATIVE.value == "Negative"
    assert SentimentLabel.NEUTRAL.value == "Neutral"