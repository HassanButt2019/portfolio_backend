from sqlalchemy import Table, Column, String
from app.schemas.metadata import metadata





# Define the "projects" table
projects_table = Table(
    "projects",
    metadata,
    Column("id", String, primary_key=True),  # Unique project ID
    Column("title", String, nullable=False),
    Column("description", String, nullable=False),
    Column("technologies", String),  # Comma-separated list of technologies
    Column("github_link", String, nullable=False),
    Column("live_demo_link", String),  # Optional demo link
)
