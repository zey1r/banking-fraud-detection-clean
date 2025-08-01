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

The API will be available at: http://localhost:8000

## 📁 Project Structure

```
banking-fraud-clean-fixed/
├── routers/           # API endpoints
│   ├── auth.py        # Authentication routes
│   ├── fraud_detection.py  # Fraud detection routes
│   └── health.py      # Health check routes
├── schemas/           # Pydantic schemas
│   ├── auth.py        # Auth schemas
│   └── fraud.py       # Fraud detection schemas
├── models/            # Database models & ML model
│   ├── database.py    # SQLAlchemy models
│   └── fraud_model.joblib # Trained ML model
├── security/          # Security modules
│   ├── auth_security.py   # Password hashing
│   └── jwt_security.py    # JWT tokens
├── config.py          # Configuration settings
├── database.py        # Database connection
├── main.py           # Application entry point
└── requirements.txt   # Dependencies
```

## 🔗 API Endpoints

- `GET /` - API root
- `GET /docs` - Interactive API documentation
- `GET /api/v1/health` - Health check
- `POST /api/v1/auth/login` - User authentication
- `POST /api/v1/fraud/predict` - Fraud prediction
- `GET /api/v1/fraud/history` - Transaction history
- `GET /api/v1/fraud/stats` - Fraud statistics

## 🛡️ Security Features

- JWT authentication
- Password hashing with bcrypt
- Environment-based configuration
- Input validation with Pydantic
- CORS middleware

## 📊 Machine Learning

- Fraud detection using RandomForest model
- Real-time prediction API
- Risk scoring system (LOW/MEDIUM/HIGH)
- Model fallback to rule-based system

## 🔧 Configuration

Edit `.env` file to configure:
- Database connection
- JWT secrets
- ML model settings

## ✅ Testing

```bash
# Test the API
curl http://localhost:8000/docs

# Health check
curl http://localhost:8000/api/v1/health

# Fraud prediction
curl -X POST "http://localhost:8000/api/v1/fraud/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "transaction_id": "TEST001",
    "amount": 15000,
    "merchant_category": 5411,
    "customer_id": "CUST001",
    "is_weekend": false,
    "is_night_time": true
  }'
```

## 📝 License

MIT License
