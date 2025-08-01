"""
Fraud detection schemas
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class FraudRequest(BaseModel):
    """Fraud detection request schema"""
    transaction_id: str
    amount: float
    merchant_category: int
    customer_id: str
    is_weekend: bool = False
    is_night_time: bool = False


class FraudResponse(BaseModel):
    """Fraud detection response schema"""
    transaction_id: str
    is_fraud: bool
    fraud_score: float
    risk_level: str
    timestamp: datetime


class TransactionHistory(BaseModel):
    """Transaction history schema"""
    transaction_id: str
    amount: float
    is_fraud: bool
    fraud_score: float
    timestamp: datetime
