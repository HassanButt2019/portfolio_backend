from sqlalchemy import Table, Column, String, Text, DateTime, MetaData, func
from app.schemas.metadata import metadata

# Define the "contact" table
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
