from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional

class MailRequest(BaseModel):
    to: List[EmailStr]
    subject: str
    template: Optional[str] = "default.html"
    variables: Dict[str, str]
