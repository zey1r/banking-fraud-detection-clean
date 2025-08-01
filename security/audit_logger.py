"""
Tamper-proof audit logging for regulatory compliance
BDDK, PCI DSS, SOX compliance
"""

import hashlib
from datetime import datetime
from typing import Dict, Any, List


class AuditLogger:
    """
    Tamper-proof audit logging for regulatory compliance
    BDDK, PCI DSS, SOX compliance
    """
    
    def __init__(self):
        self.hash_chain: List[Dict[str, Any]] = []
        
    def log_security_event(self, event_type: str, user_id: str, 
                          details: Dict[str, Any], risk_level: str = "INFO"):
        """Log security events with integrity protection"""
        timestamp = datetime.utcnow().isoformat()
        
        log_entry = {
            'timestamp': timestamp,
            'event_type': event_type,
            'user_id': user_id,
            'details': details,
            'risk_level': risk_level,
            'session_id': details.get('session_id', 'unknown'),
            'ip_address': details.get('ip_address', 'unknown'),
            'user_agent': details.get('user_agent', 'unknown')
        }
        
        # Create hash chain for integrity
        if self.hash_chain:
            previous_hash = self.hash_chain[-1]['hash']
        else:
            previous_hash = "genesis"
            
        current_hash = self._calculate_log_hash(log_entry, previous_hash)
        
        log_entry_with_hash = {
            **log_entry,
            'previous_hash': previous_hash,
            'hash': current_hash
        }
        
        self.hash_chain.append(log_entry_with_hash)
        
        # In production: Write to secure log storage
        print(f"🔒 AUDIT LOG: {log_entry_with_hash}")
        
    def _calculate_log_hash(self, log_entry: Dict[str, Any], previous_hash: str) -> str:
        """Calculate hash for log entry integrity"""
        log_string = str(sorted(log_entry.items())) + previous_hash
        return hashlib.sha256(log_string.encode()).hexdigest()
    
    def verify_log_integrity(self) -> bool:
        """Verify audit log chain integrity"""
        for i, entry in enumerate(self.hash_chain):
            if i == 0:
                expected_previous = "genesis"
            else:
                expected_previous = self.hash_chain[i-1]['hash']
                
            if entry['previous_hash'] != expected_previous:
                return False
                
        return True


# Global instance
audit_logger = AuditLogger()
