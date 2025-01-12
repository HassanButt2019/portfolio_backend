from sqlalchemy import Table, Column, String, Date
from app.schemas.metadata import metadata



# Define the "experience" table
experience_table = Table(
    "experience",
    metadata,
    Column("id", String, primary_key=True),  # Unique experience ID
    Column("title", String, nullable=False),  # Job title
    Column("company", String, nullable=False),  # Company name
    Column("start_date", Date, nullable=False),  # Start date
    Column("end_date", Date),  # End date (nullable for ongoing jobs)
    Column("responsibilities", String),  # Comma-separated responsibilities
    Column("technologies", String),  # Comma-separated technologies
)
