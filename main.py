"""
Banking Fraud Detection API - Main Application
Simple and clean main entry point following smart_stock pattern
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from config import settings
from database import engine, create_tables
from routers import fraud_detection, auth, health


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan management"""
    # Startup
    create_tables()
    yield
    # Shutdown
    pass


# Create FastAPI application
app = FastAPI(
    title="Banking Fraud Detection API",
    description="Enterprise-grade fraud detection system",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api/v1", tags=["Health"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(fraud_detection.router, prefix="/api/v1/fraud", tags=["Fraud Detection"])


@app.get("/")
async def root():
    """API Root endpoint"""
    return {
        "message": "Banking Fraud Detection API",
        "version": "1.0.0",
        "status": "active",
        "docs": "/docs",
        "health": "/api/v1/health"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
