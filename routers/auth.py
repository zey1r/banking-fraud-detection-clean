"""
Authentication endpoints
"""

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer
from schemas.auth import LoginRequest, LoginResponse
from security.jwt_security import create_access_token, verify_token

router = APIRouter()
security = HTTPBearer()


@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """User authentication endpoint"""
    
    # Simple mock authentication (replace with real auth)
    if request.username == "admin" and request.password == "password":
        access_token = create_access_token(
            data={"sub": request.username, "role": "admin"}
        )
        return LoginResponse(
            access_token=access_token,
            token_type="bearer",
            user_id="admin",
            role="admin"
        )
    
    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )


@router.get("/me")
async def get_current_user(token: str = Depends(security)):
    """Get current user information"""
    
    payload = verify_token(token.credentials)
    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    
    return {
        "user_id": payload.get("sub"),
        "role": payload.get("role"),
        "status": "active"
    }
