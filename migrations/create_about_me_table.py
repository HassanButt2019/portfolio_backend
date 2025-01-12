import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import asyncio
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import inspect
from app.schemas.metadata import metadata
from app.schemas.about import about_me_table
from app.schemas.projects import projects_table
from app.schemas.experience import experience_table
from app.schemas.contact import contact_table

# Add the project root directory to sys.path

# Load environment variables
load_dotenv()

# Get the database URL from the .env file
DATABASE_URL = os.getenv("DATABASE_URL")

# Create an async engine
engine = create_async_engine(DATABASE_URL, echo=True)


def table_exists(connection, table_name):
    """Check if a table exists in the database."""
    inspector = inspect(connection)
    return table_name in inspector.get_table_names()


async def create_table(table):
    """Create a table if it does not already exist."""
    async with engine.begin() as conn:
        if not await conn.run_sync(lambda conn: table_exists(conn, table.name)):
            await conn.run_sync(table.create)
            print(f"Table '{table.name}' created successfully.")
        else:
            print(f"Table '{table.name}' already exists.")


async def create_all_tables():
    """Run all table creation tasks."""
    await asyncio.gather(
        create_table(about_me_table),
        create_table(projects_table),
        create_table(experience_table),
        create_table(experience_table),

    )

async def create_all_tables():
    """Run all table creation tasks."""
    print("Before creating tables, metadata contains:", metadata.tables.keys())
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    print("All tables created successfully.")
if __name__ == "__main__":
    asyncio.run(create_all_tables())
