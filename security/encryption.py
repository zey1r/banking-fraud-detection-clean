"""
Data encryption and decryption utilities
"""

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from typing import Dict, Any


class DataEncryption:
    """Symmetric encryption for sensitive data"""
    
    def __init__(self):
        # AES-256 key for symmetric encryption
        self.symmetric_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.symmetric_key)
    
    def encrypt_sensitive_data(self, data: str) -> str:
        """Encrypt sensitive data (PII, financial data)"""
        encrypted_data = self.cipher_suite.encrypt(data.encode())
        return base64.b64encode(encrypted_data).decode()
    
    def decrypt_sensitive_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data"""
        encrypted_bytes = base64.b64decode(encrypted_data.encode())
        decrypted_data = self.cipher_suite.decrypt(encrypted_bytes)
        return decrypted_data.decode()


class DigitalSignature:
    """RSA digital signatures for transaction integrity"""
    
    def __init__(self):
        # RSA-4096 for asymmetric encryption
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096
        )
        self.public_key = self.private_key.public_key()
    
    def sign_transaction(self, transaction_data: Dict[str, Any]) -> str:
        """Digital signature for transaction integrity"""
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding
        
        transaction_string = str(sorted(transaction_data.items()))
        signature = self.private_key.sign(
            transaction_string.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode()
    
    def verify_transaction_signature(self, transaction_data: Dict[str, Any], signature: str) -> bool:
        """Verify transaction digital signature"""
        try:
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.asymmetric import padding
            
            transaction_string = str(sorted(transaction_data.items()))
            signature_bytes = base64.b64decode(signature.encode())
            
            self.public_key.verify(
                signature_bytes,
                transaction_string.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False


# Global instances
data_encryption = DataEncryption()
digital_signature = DigitalSignature()
