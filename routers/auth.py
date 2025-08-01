"""
Authentication endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from datetime import datetime, timedelta
import jwt

from config import settings
from schemas.auth import TokenResponse, LoginRequest

router = APIRouter()
security = HTTPBearer()


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    """User authentication endpoint"""
    
    # Simple authentication logic (replace with real auth)
    if request.username == "admin" and request.password == "admin123":
        
        # Create JWT token
        payload = {
            "sub": request.username,
            "exp": datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        }
        
        token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        
        return TokenResponse(
            access_token=token,
            token_type="bearer",
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials"
    )


@router.get("/verify")
async def verify_token(token: str = Depends(security)):
    """Token verification endpoint"""
    try:
        payload = jwt.decode(
            token.credentials, 
            settings.JWT_SECRET_KEY, 
            algorithms=[settings.JWT_ALGORITHM]
        )
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username, "valid": True}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
