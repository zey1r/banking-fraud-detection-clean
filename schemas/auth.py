"""
Authentication schemas
"""

from pydantic import BaseModel


class LoginRequest(BaseModel):
    """Login request schema"""
    username: str
    password: str


class LoginResponse(BaseModel):
    """Login response schema"""
    access_token: str
    token_type: str
    user_id: str
    role: str
