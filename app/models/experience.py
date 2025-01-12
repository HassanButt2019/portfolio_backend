from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Experience(BaseModel):
    id: Optional[str] = None   # Unique identifier (auto-generated)
    title: str  # Job title (e.g., Backend Developer)
    company: str  # Company name
    start_date: date  # Start date of employment
    end_date: Optional[date]  # End date (nullable for ongoing jobs)
    responsibilities: List[str]  # List of key responsibilities
    technologies: List[str]  # List of technologies used
