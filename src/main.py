import os
from fastapi import FastAPI
from src.infrastructure.adapters.outgoing.sentiment_analysis_adapter import SentimentAnalysisAdapter
from src.application.use_cases.analyse_sentiment_use_case import AnalyzeSentimentUseCase
from src.infrastructure.adapters.ingoing.routers import sentiment_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Financial Sentiment API",
        description="Financial Sentiment API Service",
        version="1.0.0"
    )

    model_path = os.getenv("MODEL_PATH", "models/sentiment_analysis_model")
    try:
        model_adapter = SentimentAnalysisAdapter(model_path=model_path)
    except Exception as e:
        print(f"Composition Error: {e}")
        model_adapter = None

    analyze_use_case = AnalyzeSentimentUseCase(model_port=model_adapter)

    app.state.analyze_sentiment_use_case = analyze_use_case

    app.include_router(sentiment_router)

    @app.get("/")
    def health_check():
        return {"status": "online", "model_loaded": model_adapter is not None}

    return app

app = create_app()