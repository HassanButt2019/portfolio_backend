from sqlalchemy import  Table, Column, String
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, String, Text, DateTime, MetaData, func,Date , Boolean
from sqlalchemy import (
    Table, Column, MetaData, String, Integer, DateTime, JSON, Enum, ForeignKey, CheckConstraint
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid
import enum


metadata = MetaData()
# Define the "about_me" table
about_me_table = Table(
    "about_me",  # Table name
    metadata,
    Column("id", String, primary_key=True),  # Unique identifier
    Column("name", String),  # Name
    Column("bio", String),  # Biography
    Column("skills", String),  # Comma-separated skills
)

contact_table = Table(
    "contact",
    metadata,
    Column("id", String, primary_key=True),  # Unique message ID
    Column("name", String, nullable=False),  # Sender's name
    Column("email", String, nullable=False),  # Sender's email
    Column("message", Text, nullable=False),  # Message content
    Column("linkedin", String),  # LinkedIn profile URL
    Column("github", String),  # GitHub profile URL
    Column("created_at", DateTime, default=func.now(), nullable=False),  # Timestamp
)





# Define the "experience" table ===============================================================
experience_table = Table(
    "experience",
    metadata,
    
    # Unique experience ID
    Column("id", Integer, primary_key=True, autoincrement=True),

    # Basic experience details
    Column("title", String, nullable=False),  # Job title
    Column("description", String, nullable=True),  # Job description

    # Nested JSON objects
    Column("company", JSONB, nullable=False),  # Company details as JSON
    Column("location", JSONB, nullable=True),  # Location details as JSON

    # Employment type and status
    Column("type", String, nullable=False),  # Employment type: full-time, part-time, etc.
    Column("current", String, nullable=False, server_default="false"),  # Whether the job is current

    # Dates
    Column("start_date", Date, nullable=False),  # Start date
    Column("end_date", Date, nullable=True),  # End date (nullable for ongoing jobs)

    # Responsibilities and technologies
    Column("responsibilities", JSONB, nullable=True),  # List of responsibilities as JSON
    Column("technologies", JSONB, nullable=True),  # List of technologies as JSON

    # Indexes and constraints
    CheckConstraint("end_date IS NULL OR end_date >= start_date", name="check_end_date"),
)








#=============================================================== projects ===============================================================

# Define enums for PostgreSQL
class VisibilityEnum(enum.Enum):
    PUBLIC = "public"
    PRIVATE = "private"
projects_table = Table(
    "projects",
    metadata,
    # Unique project ID
    Column("id", Integer, primary_key=True, autoincrement=True),

    # Basic project details
    Column("title", String, nullable=False),
    Column("description", String, nullable=True),
    Column("short_description", String, nullable=True),

    # Category, status, priority, and visibility
    Column("category", JSONB, nullable=True),  # Flexible JSON structure
    Column("status", JSONB, nullable=True),  # JSONB for better indexing
    Column("priority", JSONB, nullable=True),
    # Column("visibility", Enum(VisibilityEnum), nullable=False, default=VisibilityEnum.PUBLIC),

    # Dates
    Column("start_date", DateTime, nullable=True),
    Column("end_date", DateTime, nullable=True),
    Column("last_updated", DateTime, nullable=False, server_default="now()"),

    # Technical details
    Column("technologies", JSONB, nullable=True),
    Column("architecture", String, nullable=True),
    Column("deployment", JSONB, nullable=True),
    Column("repository", JSONB, nullable=True),

    # Team and collaboration
    Column("team", JSONB, nullable=True),
    Column("collaborators", JSONB, nullable=True),

    # Progress and metrics
    Column("progress", Integer, CheckConstraint("progress >= 0 AND progress <= 100"), nullable=True),
    Column("metrics", JSONB, nullable=True),
    Column("milestones", JSONB, nullable=True),
    Column("tasks", JSONB, nullable=True),

    # Media and documentation
    Column("images", JSONB, nullable=True),
    Column("documentation", String, nullable=True),
    Column("links", JSONB, nullable=True),

    # Indexes for faster queries
    CheckConstraint("end_date IS NULL OR end_date >= start_date", name="check_end_date"),
)
repo_languages_table = Table(
    "repo_languages",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("repo_name", String, nullable=False),
    Column("languages", JSON, nullable=False),  # JSON to store language stats
    Column("last_fetched", DateTime, default=func.now(), nullable=False),
)