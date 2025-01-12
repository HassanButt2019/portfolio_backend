from sqlalchemy import  Table, Column, String
from app.schemas.metadata import metadata

# Define the "about_me" table
about_me_table = Table(
    "about_me",  # Table name
    metadata,
    Column("id", String, primary_key=True),  # Unique identifier
    Column("name", String),  # Name
    Column("bio", String),  # Biography
    Column("skills", String),  # Comma-separated skills
)
