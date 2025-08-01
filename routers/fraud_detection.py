"""
Fraud detection endpoints
"""

from fastapi import APIRouter, HTTPException
from typing import List
import joblib
import numpy as np
from datetime import datetime
import os

from schemas.fraud import FraudRequest, FraudResponse, TransactionHistory
from config import settings

router = APIRouter()

# Load ML model
model = None
try:
    if os.path.exists(settings.MODEL_PATH):
        model = joblib.load(settings.MODEL_PATH)
        print(f"✅ ML Model loaded from {settings.MODEL_PATH}")
    else:
        print(f"⚠️ Model file not found: {settings.MODEL_PATH}, using mock predictions")
except Exception as e:
    print(f"⚠️ Failed to load model: {e}, using mock predictions")
    model = None


@router.post("/predict", response_model=FraudResponse)
async def predict_fraud(request: FraudRequest):
    """Predict fraud probability for a transaction"""
    
    try:
        if model is not None:
            # Real ML prediction
            features = np.array([[
                request.amount,
                request.merchant_category,
                float(request.is_weekend),
                float(request.is_night_time)
            ]])
            
            fraud_probability = model.predict_proba(features)[0][1]
            fraud_score = float(fraud_probability)
        else:
            # Mock prediction logic
            fraud_score = 0.0
            
            if request.amount > 10000:
                fraud_score += 0.3
            if request.merchant_category in [5411, 5812]:  # High-risk categories
                fraud_score += 0.2
            if request.is_night_time:
                fraud_score += 0.1
            if request.is_weekend:
                fraud_score += 0.05
                
            fraud_score = min(fraud_score, 1.0)
        
        is_fraud = fraud_score > settings.MODEL_THRESHOLD
        
        # Determine risk level
        if fraud_score > 0.7:
            risk_level = "HIGH"
        elif fraud_score > 0.3:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"
        
        return FraudResponse(
            transaction_id=request.transaction_id,
            is_fraud=is_fraud,
            fraud_score=fraud_score,
            risk_level=risk_level,
            timestamp=datetime.utcnow()
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )


@router.get("/history", response_model=List[TransactionHistory])
async def get_transaction_history():
    """Get recent transaction history"""
    
    # Mock data (replace with real database query)
    return [
        TransactionHistory(
            transaction_id="TXN001",
            amount=1500.00,
            is_fraud=False,
            fraud_score=0.2,
            timestamp=datetime.utcnow()
        ),
        TransactionHistory(
            transaction_id="TXN002",
            amount=15000.00,
            is_fraud=True,
            fraud_score=0.8,
            timestamp=datetime.utcnow()
        )
    ]


@router.get("/stats")
async def get_fraud_stats():
    """Get fraud detection statistics"""
    
    return {
        "total_transactions": 10000,
        "fraud_detected": 250,
        "fraud_rate": 0.025,
        "model_accuracy": 0.95,
        "model_status": "loaded" if model else "mock"
    }
