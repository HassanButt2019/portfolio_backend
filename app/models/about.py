from pydantic import BaseModel
from typing import List

class AboutMe(BaseModel):
    id: str  # Unique ID for the entry (can be pre-defined or auto-generated)
    name: str
    bio: str
    skills: List[str]
