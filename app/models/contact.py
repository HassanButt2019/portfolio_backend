from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional
from datetime import datetime


class Contact(BaseModel):
    id: Optional[int] = None  # Auto-generated ID (optional for POST)
    name: str  # Sender's name
    email: EmailStr  # Sender's email
    message: str  # Message content
    linkedin: Optional[str] = None  # LinkedIn profile URL
    github: Optional[str] = None  # GitHub profile URL
    created_at: Optional[datetime] = None  # Timestamp when the message was sent
