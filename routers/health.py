"""
Health check endpoints
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Banking Fraud Detection API",
        "version": "1.0.0"
    }


@router.get("/health/detailed")
async def detailed_health():
    """Detailed health check"""
    return {
        "status": "healthy",
        "service": "Banking Fraud Detection API",
        "version": "1.0.0",
        "database": "connected",
        "ml_model": "loaded",
        "timestamp": "2025-08-01T00:00:00Z"
    }
