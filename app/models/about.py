from pydantic import BaseModel
from typing import List, Optional

class AboutMe(BaseModel):
    id: Optional[int] = None  # Auto-generated ID (optional for POST)
    name: str
    bio: str
    skills: List[str]
