from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional, Any

class MailRequest(BaseModel):
    to: List[EmailStr]
    subject: str
    template: Optional[str] = "default.html"
    variables: Dict[str, Any]
