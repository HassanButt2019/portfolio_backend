from numbers import Integral
from sqlalchemy import  Table, Column, String
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, String, Text, DateTime, MetaData, func,Date


metadata = MetaData()
# Define the "about_me" table
about_me_table = Table(
    "about_me",  # Table name
    metadata,
    Column("id", Integral, primary_key=True, autoincrement=True),  # Auto-incrementing primary key
    Column("name", String),  # Name
    Column("bio", String),  # Biography
    Column("skills", String),  # Comma-separated skills
)

contact_table = Table(
    "contact",
    metadata,
    Column("id", Integral, primary_key=True, autoincrement=True),  # Auto-incrementing primary key
    Column("name", String, nullable=False),  # Sender's name
    Column("email", String, nullable=False),  # Sender's email
    Column("message", Text, nullable=False),  # Message content
    Column("linkedin", String),  # LinkedIn profile URL
    Column("github", String),  # GitHub profile URL
    Column("created_at", DateTime, default=func.now(), nullable=False),  # Timestamp
)


# Define the "experience" table
experience_table = Table(
    "experience",
    metadata,
    Column("id", Integral, primary_key=True, autoincrement=True),  # Auto-incrementing primary key
    Column("title", String, nullable=False),  # Job title
    Column("company", String, nullable=False),  # Company name
    Column("start_date", Date, nullable=False),  # Start date
    Column("end_date", Date),  # End date (nullable for ongoing jobs)
    Column("responsibilities", String),  # Comma-separated responsibilities
    Column("technologies", String),  # Comma-separated technologies
)

projects_table = Table(
    "projects",
    metadata,
    Column("id", Integral, primary_key=True, autoincrement=True),  # Auto-incrementing primary key
    Column("title", String(255), nullable=False),
    Column("description", Text, nullable=False),
    Column("technologies", Text, nullable=True),
    Column("github_link", String(255), nullable=False),
    Column("live_demo_link", String(255), nullable=True),
)