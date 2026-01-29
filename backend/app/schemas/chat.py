from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    question: str
    session_id: str = "default-session"  # Added session support

class ChatResponse(BaseModel):
    answer: str
    sources: Optional[List[str]] = []  # Added for traceability