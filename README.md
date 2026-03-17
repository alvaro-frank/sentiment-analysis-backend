# Financial Sentiment Analysis - Backend

![CI Status](https://github.com/alvaro-frank/sentiment-analysis-backend/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0%2B-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)
![MLflow](https://img.shields.io/badge/Model-MLflow%20PyFunc-0194E2?logo=mlflow&logoColor=white)
![TensorFlow](https://img.shields.io/badge/Engine-TensorFlow--CPU-orange?logo=tensorflow&logoColor=white)

A production-grade NLP inference service for financial text. This project serves a lightweight **Bi-LSTM** model (distilled from FinBERT) via a high-performance FastAPI backend. It follows **Clean Architecture** principles to decouple core business logic from technical infrastructure and ML frameworks.

## 📂 Project Structure
```bash
├── src/
│   ├── application/        # Application Logic (Use Cases & DTOs)
│   │   ├── dtos/           # Data Transfer Objects for internal mapping
│   │   ├── ports/          # Interfaces for Outbound Adapters (Model Port)
│   │   └── use_cases/      # Business logic orchestrators (Analyze Sentiment)
│   ├── domain/             # Business Core (Pure Entities & Enums)
│   │   └── entities.py     # SentimentResult and SentimentLabel definitions
│   ├── infrastructure/     # Technical Details & External Integrations
│   │   ├── adapters/       # Implementation of Ports
│   │   │   ├── ingoing/    # FastAPI Routers (HTTP Entry points)
│   │   │   └── outgoing/   # MLflow PyFunc Adapter for model inference
│   │   └── schemas/        # Pydantic Schemas for Request/Response validation
│   └── main.py             # Application entry point & Dependency Injection
├── models/                 # Versioned ML models
├── tests/                  # Automated Test Suite
│   ├── unit/               # Domain, Use Case, and Adapter unit tests
│   └── integration/        # End-to-end API flow tests with real models
├── Dockerfile              # Container image definition
├── docker-compose.yml      # Service orchestration
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🛠️ Setup & Requirements

- `Python 3.10`
- `Docker` and `Docker Compose`

1. **Clone the repository**
```bash
git clone [https://github.com/alvaro-frank/sentiment-analysis-backend.git](https://github.com/alvaro-frank/sentiment-analysis-backend.git)
cd sentiment-analysis-backend
```

2. **Create and activate Virtual Environment**:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## ⚡ Quick Start

To run the API using **Docker** (recommended):
```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`. You can access the interactive Swagger documentation at `http://localhost:8000/docs`.

To run locally for development:
```bash
set PYTHONPATH=.
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

## 🔌 API Usage

The primary endpoint is `POST /predict`.

**Request Payload**:
```bash
{
  "text": "The company reported a 20% increase in revenue."
}
```

**Response Example**:
```bash
{
  "text": "The company reported a 20% increase in revenue.",
  "sentiment_score": 0.6542,
  "label": "Positive"
}
```

## 🧠 Methodology

**Clean Architecture & MLflow Integration**

This backend acts as a dedicated serving layer, isolated from the training pipeline.

1. **Separation of Concerns**: The domain layer defines what a "Sentiment" is, while the infrastructure layer handles how the MLflow model is loaded and executed.
2. **MLflow PyFunc**: We use the mlflow.pyfunc loader to load an encapsulated model. This package includes the trained weights, the tokenizer, and the specific domain-specific preprocessing logic (negation preservation and number normalization).
3. **DTO Mapping**: Data is strictly mapped from Web Schemas (Pydantic) to Application DTOs (Dataclasses) to ensure that changes in the API contract do not break the core logic.

## 🧪 Testing

The project implements a tiered testing strategy to ensure reliability:
```bash
# Set PYTHONPATH and run tests
set PYTHONPATH=.
pytest tests/ -v
```

## ⚙️ CI/CD Pipeline

The project includes a GitHub Actions workflow that automates quality control:

- **Linting**: Enforces PEP8 standards using `flake8`.
- **Automated Testing**: Executes the full `pytest` suite (Unit + Integration) on every push.
- **Build Verification**: Ensures the Docker image builds successfully in a clean environment.

## 🐳 Docker Support

The application is fully containerized and optimized for production:

- **Isolated Inference**: Uses `tensorflow-cpu` to reduce image size and resource overhead.
- **Hot-Reload**: The `docker-compose.yml` is configured with volumes for a seamless developer experience.
- **Autonomy**: The model is embedded within the image, removing any runtime dependency on an external MLflow Tracking Server.
