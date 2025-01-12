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
                CREATE TABLE IF NOT EXISTS projects (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    description TEXT NOT NULL,
                    technologies TEXT,
                    github_link VARCHAR(255) NOT NULL,
                    live_demo_link VARCHAR(255)
                );
            """),
            text("""
                CREATE TABLE IF NOT EXISTS about_me (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    bio TEXT NOT NULL,
                    skills TEXT
                );
            """),
            text("""
                CREATE TABLE IF NOT EXISTS contact (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    message TEXT NOT NULL,
                    linkedin VARCHAR(255),
                    github VARCHAR(255),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """),
            text("""
                CREATE TABLE IF NOT EXISTS experience (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    company VARCHAR(255) NOT NULL,
                    start_date DATE NOT NULL,
                    end_date DATE,
                    responsibilities TEXT,
                    technologies TEXT
                );
            """),
        ]

        # Execute each query
        for query in queries:
            await conn.execute(query)