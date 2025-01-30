from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import date

from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class Location(BaseModel):
    city: Optional[str]
    country: Optional[str]
    remote: Optional[bool]


class Company(BaseModel):
    id: Optional[int]  # Assuming company details include an ID
    name: Optional[str]
    logo: Optional[str]
    industry: Optional[str]
    website: Optional[str]
    size: Optional[str]
    location: Optional[Location]


class Experience(BaseModel):
    id: Optional[int]  # Auto-incremented ID
    title: str  # Job title
    description: Optional[str]  # Job description
    company: Company  # Company details as JSON
    location: Optional[Location]  # Location details as JSON
    type: str  # Employment type: full-time, part-time, etc.
    current: bool  # Whether the job is current (converted from "true"/"false")
    start_date: date  # Start date
    end_date: Optional[date]  # End date (nullable for ongoing jobs)
    responsibilities: Optional[List[str]]  # List of responsibilities as JSON
    technologies: Optional[List[str]]  # List of technologies as JSON
