"""
Fraud detection schemas
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class FraudRequest(BaseModel):
    """Fraud detection request schema"""
    transaction_id: str = Field(..., description="Unique transaction identifier")
    amount: float = Field(..., gt=0, description="Transaction amount")
    merchant_category: int = Field(..., description="Merchant category code")
    is_weekend: bool = Field(default=False, description="Transaction on weekend")
    is_night_time: bool = Field(default=False, description="Transaction at night")
    customer_id: Optional[str] = Field(None, description="Customer identifier")


class FraudResponse(BaseModel):
    """Fraud detection response schema"""
    transaction_id: str
    is_fraud: bool
    fraud_score: float = Field(..., ge=0, le=1, description="Fraud probability score")
    risk_level: str = Field(..., description="Risk level: LOW, MEDIUM, HIGH")
    timestamp: datetime


class TransactionHistory(BaseModel):
    """Transaction history schema"""
    transaction_id: str
    amount: float
    is_fraud: bool
    fraud_score: float
    timestamp: datetime
