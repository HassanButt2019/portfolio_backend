from pydantic import BaseModel
from typing import List, Optional

class AboutMe(BaseModel):
    id: Optional[str] = None   # Unique ID for the entry (can be pre-defined or auto-generated)
    name: str
    bio: str
    skills: List[str]
