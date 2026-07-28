from pydantic import BaseModel
from datetime import datetime


class Document(BaseModel):
    filename: str
    content: str
    uploaded_at: datetime = datetime.utcnow()
    
class ChatRequest(BaseModel):
    question: str    