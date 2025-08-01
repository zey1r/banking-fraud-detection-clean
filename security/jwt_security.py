"""
JWT token management for enterprise authentication
"""

import jwt
import secrets
from datetime import datetime, timedelta
from typing import Optional, Dict, Any


class JWTManager:
    """Enterprise-grade JWT token management"""
    
    def __init__(self):
        self.session_timeout = 1800  # 30 minutes
        self.algorithm = 'HS512'  # More secure than HS256
        self.audience = 'banking-fraud-detection'
        self.issuer = 'verivigil-enterprise'
    
    def generate_enterprise_jwt(self, payload: Dict[str, Any], secret_key: str) -> str:
        """Generate enterprise-grade JWT with enhanced security"""
        # Add security claims
        now = datetime.utcnow()
        enhanced_payload = {
            **payload,
            'iat': now,
            'exp': now + timedelta(seconds=self.session_timeout),
            'nbf': now,
            'jti': secrets.token_urlsafe(32),  # JWT ID for tracking
            'aud': self.audience,
            'iss': self.issuer
        }
        
        return jwt.encode(
            enhanced_payload,
            secret_key,
            algorithm=self.algorithm,
            headers={'typ': 'JWT', 'alg': self.algorithm}
        )
    
    def validate_enterprise_jwt(self, token: str, secret_key: str) -> Optional[Dict[str, Any]]:
        """Validate JWT with enhanced security checks"""
        try:
            payload = jwt.decode(
                token,
                secret_key,
                algorithms=[self.algorithm],
                audience=self.audience,
                issuer=self.issuer
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise SecurityException("Token expired")
        except jwt.InvalidTokenError:
            raise SecurityException("Invalid token")


class SecurityException(Exception):
    """Custom security exception for enterprise error handling"""
    pass


# Global instance
jwt_manager = JWTManager()
