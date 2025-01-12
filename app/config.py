# Placeholder for project settings

from app.services.db import database
from sqlalchemy import text


class Settings:
    PROJECT_NAME: str = "My FastAPI Project"
    DATABASE_URL: str = "sqlite:///./test.db"


settings = Settings()


async def initialize_tables():
    """Create tables if they do not exist."""
    async with database.connection() as conn:
        # List of table creation queries
        queries = [
            text("""
                CREATE TABLE IF NOT EXISTS about_me (
                    id VARCHAR PRIMARY KEY,  -- String-based primary key
                    name VARCHAR(255),       -- Name
                    bio TEXT,                -- Biography
                    skills TEXT              -- Comma-separated skills
                );
            """),
            text("""
                CREATE TABLE IF NOT EXISTS contact (
                    id VARCHAR PRIMARY KEY,       -- String-based primary key
                    name VARCHAR(255) NOT NULL,   -- Sender's name
                    email VARCHAR(255) NOT NULL,  -- Sender's email
                    message TEXT NOT NULL,        -- Message content
                    linkedin VARCHAR(255),        -- LinkedIn profile URL
                    github VARCHAR(255),          -- GitHub profile URL
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL -- Timestamp
                );
            """),
            text("""
                CREATE TABLE IF NOT EXISTS experience (
                    id VARCHAR PRIMARY KEY,       -- String-based primary key
                    title VARCHAR(255) NOT NULL,  -- Job title
                    company VARCHAR(255) NOT NULL,-- Company name
                    start_date DATE NOT NULL,     -- Start date
                    end_date DATE,                -- End date (nullable for ongoing jobs)
                    responsibilities TEXT,        -- Comma-separated responsibilities
                    technologies TEXT             -- Comma-separated technologies
                );
            """),
            text("""
                CREATE TABLE IF NOT EXISTS projects (
                    id VARCHAR PRIMARY KEY,       -- String-based primary key
                    title VARCHAR(255) NOT NULL,  -- Project title
                    description TEXT NOT NULL,    -- Project description
                    technologies TEXT,            -- Comma-separated list of technologies
                    github_link VARCHAR(255) NOT NULL, -- GitHub link
                    live_demo_link VARCHAR(255)   -- Optional demo link
                );
            """)
        ]

        # Execute each query
        for query in queries:
            await conn.execute(query)
