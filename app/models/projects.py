from pydantic import BaseModel ,HttpUrl
from typing import List, Optional

class Project(BaseModel):
    id: Optional[int] = None  # Auto-generated ID (optional for POST)
    title: str
    description: str
    technologies: List[str]
    github_link: Optional[HttpUrl]
    live_demo_link: Optional[HttpUrl]  # Optional demo link
