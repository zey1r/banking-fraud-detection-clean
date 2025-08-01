# Banking Fraud Detection API

Enterprise-grade fraud detection API built with FastAPI, following clean architecture principles.

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run the application
python main.py
```

## 📁 Project Structure

```
fraud_api_clean/
├── routers/           # API endpoints
│   ├── auth.py        # Authentication routes
│   ├── fraud_detection.py  # Fraud detection routes
│   └── health.py      # Health check routes
├── schemas/           # Pydantic schemas
│   ├── auth.py        # Auth schemas
│   └── fraud.py       # Fraud detection schemas
├── models/            # Database models
│   └── database.py    # SQLAlchemy models
├── config.py          # Configuration settings
├── database.py        # Database connection
├── main.py           # Application entry point
└── requirements.txt   # Dependencies
```

## 🔗 API Endpoints

- `GET /` - API root
- `GET /api/v1/health` - Health check
- `POST /api/v1/auth/login` - User authentication
- `POST /api/v1/fraud/predict` - Fraud prediction
- `GET /api/v1/fraud/history` - Transaction history

## 🛡️ Security Features

- JWT authentication
- Environment-based configuration
- Input validation with Pydantic
- CORS middleware

## 📊 Machine Learning

- Fraud detection using ML models
- Real-time prediction API
- Risk scoring system

## 🔧 Configuration

Edit `.env` file to configure:
- Database connection
- JWT secrets
- ML model settings
- CORS origins
