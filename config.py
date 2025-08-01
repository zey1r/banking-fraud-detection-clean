"""
Application configuration settings
"""

import os
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    # API Settings
    APP_NAME: str = "Banking Fraud Detection API"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./fraud_detection.db")
    
    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8080",
        "http://127.0.0.1:8000"
    ]
    
    # ML Model
    MODEL_PATH: str = os.getenv("MODEL_PATH", "./models/fraud_model.joblib")
    MODEL_THRESHOLD: float = 0.5
    
    # Monitoring
    ENABLE_MONITORING: bool = True
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"


# Global settings instance
settings = Settings()
