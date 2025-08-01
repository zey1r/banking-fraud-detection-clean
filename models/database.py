"""
Database models for fraud detection
"""

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime

from database import Base


class Transaction(Base):
    """Transaction model"""
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, unique=True, index=True)
    amount = Column(Float, nullable=False)
    merchant_category = Column(Integer, nullable=False)
    customer_id = Column(String, index=True)
    is_fraud = Column(Boolean, default=False)
    fraud_score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)


class User(Base):
    """User model"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
