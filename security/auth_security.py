"""
Password and authentication security utilities
"""

from passlib.context import CryptContext
import bcrypt
import secrets
import base64
from typing import Optional


class PasswordSecurity:
    """Password hashing and verification (PCI DSS compliant)"""
    
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def hash_password(self, password: str) -> str:
        """Hash password with bcrypt (PCI DSS compliant)"""
        return self.pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify password against hash"""
        return self.pwd_context.verify(plain_password, hashed_password)


class MFASecurity:
    """Multi-Factor Authentication utilities"""
    
    def generate_mfa_secret(self) -> str:
        """Generate MFA secret for 2FA"""
        return base64.b32encode(secrets.token_bytes(20)).decode('utf-8')
    
    def verify_totp(self, secret: str, token: str, window: int = 1) -> bool:
        """Verify TOTP token for MFA"""
        try:
            import pyotp
            totp = pyotp.TOTP(secret)
            return totp.verify(token, valid_window=window)
        except ImportError:
            # Fallback if pyotp not available
            return False


# Global instances
password_security = PasswordSecurity()
mfa_security = MFASecurity()
