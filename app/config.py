# Placeholder for project settings

from app.services.db import database
from sqlalchemy import text


class Settings:
    PROJECT_NAME: str = "My FastAPI Project"
    DATABASE_URL: str = "sqlite:///./test.db"


settings = Settings()


async def initialize_tables():
    """Create tables if they do not exist."""

    print("Initilizing tables")
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
        id SERIAL PRIMARY KEY,                  -- Auto-incrementing primary key
        title VARCHAR(255) NOT NULL,            -- Project title
        description TEXT,                       -- Project description
        short_description TEXT,                 -- Short project summary
        category JSONB,                         -- JSONB structure for category
        status JSONB,                           -- JSONB structure for status
        priority JSONB,                         -- JSONB structure for priority
        start_date TIMESTAMP,                   -- Project start date
        end_date TIMESTAMP,                     -- Project end date (nullable)
        last_updated TIMESTAMP,   -- Last updated timestamp with default current time
        technologies JSONB,                     -- JSONB array of technologies
        architecture VARCHAR(255),             -- Architecture description
        deployment JSONB,                       -- Deployment details as JSONB
        repository JSONB,                       -- Repository details as JSONB
        team JSONB,                             -- JSONB array of team members
        collaborators JSONB,                    -- JSONB array of collaborators
        progress INTEGER CHECK (progress >= 0 AND progress <= 100), -- Progress between 0 and 100
        metrics JSONB,                          -- Key-value metrics as JSONB
        milestones JSONB,                       -- List of milestones as JSONB
        tasks JSONB,                            -- List of tasks as JSONB
        images JSONB,                           -- List of image URLs as JSONB
        documentation TEXT,                     -- Documentation details
        links JSONB,                            -- Links related to the project (e.g., GitHub, live demo)

        -- Constraints
        CONSTRAINT check_end_date CHECK (end_date IS NULL OR end_date >= start_date) -- Ensure end_date is after start_date
    );
""")
        ]

        # Execute each query
        for query in queries:
            await conn.execute(query)
        
        print("Initiled tables")

