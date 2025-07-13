from databases import Database
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the database URL from the environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Initialize the database
database = Database("postgresql://postgres:1234@localhost:5432/postgres?sslmode=require")

class AboutMeDB:
    @staticmethod
    async def init():
        """Initialize the database connection."""
        await database.connect()

    @staticmethod
    async def close():
        """Close the database connection."""
        await database.disconnect()
