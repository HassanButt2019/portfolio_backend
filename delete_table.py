from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the database URL from the environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Replace with your actual table name
TABLE_NAME = "experience"

def delete_table():
    """Delete a table from the database."""
    try:
        # Connect to the database
        engine = create_engine(DATABASE_URL)
        metadata = MetaData()
        metadata.reflect(bind=engine)

        # Check if the table exists
        if TABLE_NAME in metadata.tables:
            table = metadata.tables[TABLE_NAME]
            table.drop(engine)
            print(f"Table '{TABLE_NAME}' has been deleted.")
        else:
            print(f"Table '{TABLE_NAME}' does not exist in the database.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    delete_table()
