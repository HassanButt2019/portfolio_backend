from dataclasses import Field
import uuid
from pydantic import BaseModel, conint
from pydantic import BaseModel, HttpUrl
from typing import Dict, List, Optional, Literal
from datetime import datetime
from uuid import UUID

from app.schemas.database_schema import VisibilityEnum


class Project(BaseModel):
    # Unique project ID
    id: Optional[int] = None

    # Basic project details
    title: str
    description: Optional[str]
    short_description: Optional[str]

    # Category, status, priority
    category: Optional[Dict]  # JSONB equivalent in PostgreSQL
    status: Optional[Dict]  # JSONB equivalent
    priority: Optional[Dict]  # JSONB equivalent

    # Dates
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    last_updated: Optional[datetime] = None

    # Technical details
    technologies: Optional[List[str]]  # Stored as JSONB
    architecture: Optional[str]
    deployment: Optional[Dict]  # JSONB equivalent
    repository: Optional[Dict]  # JSONB equivalent

    # Team and collaboration
    team: Optional[List[str]]  # Stored as JSONB
    collaborators: Optional[List[str]]  # Stored as JSONB

    # Progress and metrics
    progress: Optional[conint(ge=0, le=100)]  # Integer with range constraints
    metrics: Optional[Dict]  # JSONB equivalent
    milestones: Optional[List[Dict]]  # Stored as JSONB
    tasks: Optional[List[Dict]]  # Stored as JSONB

    # Media and documentation
    images: Optional[List[str]]  # Stored as JSONB
    documentation: Optional[str]
    links: Optional[Dict]  # JSONB equivalent