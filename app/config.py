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
            # text("""
            #     CREATE TABLE IF NOT EXISTS repo_languages (
            #         id SERIAL PRIMARY KEY,  -- String-based primary key
            #         repo_name VARCHAR(255),       -- Name
            #         languages JSONB,                -- Languages
            #         last_fetched  DATE            -- Comma-separated skills
            #     );
            # """),
            # text("""
            #     CREATE TABLE IF NOT EXISTS about_me (
            #         id VARCHAR PRIMARY KEY,  -- String-based primary key
            #         name VARCHAR(255),       -- Name
            #         bio TEXT,                -- Biography
            #         skills TEXT              -- Comma-separated skills
            #     );
            # """),
            # text("""
            #     CREATE TABLE IF NOT EXISTS contact (
            #         id VARCHAR PRIMARY KEY,       -- String-based primary key
            #         name VARCHAR(255)  ,   -- Sender's name
            #         email VARCHAR(255)  ,  -- Sender's email
            #         message TEXT  ,        -- Message content
            #         linkedin VARCHAR(255),        -- LinkedIn profile URL
            #         github VARCHAR(255),          -- GitHub profile URL
            #         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp
            #     );
            # """),

            # ==============================experience schema========================================
            text("""
            CREATE TABLE IF NOT EXISTS experience (
                id SERIAL PRIMARY KEY,                -- Auto-incremented ID
                title VARCHAR(255) NOT NULL,          -- Job title
                company JSONB NOT NULL,               -- Company details as JSON
                type VARCHAR(50) CHECK (type IN ('full-time', 'part-time', 'freelance', 'contract', 'internship')), -- Employment type
                location JSONB,                       -- Location details as JSON
                start_date DATE NOT NULL,             -- Start date
                end_date DATE,                        -- End date (nullable for ongoing jobs)
                current BOOLEAN DEFAULT FALSE,        -- Is the job current?
                description TEXT,                     -- Description of the role
                responsibilities JSONB,               -- List of responsibilities as JSON
                technologies JSONB,                   -- List of technologies as JSON
                achievements JSONB,                   -- List of achievements as JSON
                projects JSONB                        -- List of projects as JSON
            );
            """),


            # ==============================project schema========================================
            text("""
    CREATE TABLE IF NOT EXISTS projects (
        id SERIAL PRIMARY KEY,                  -- Auto-incrementing primary key
        title VARCHAR(255)  ,            -- Project title
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
