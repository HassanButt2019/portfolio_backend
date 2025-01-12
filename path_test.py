import asyncio
import asyncpg
import os

async def test_connection():
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1234@localhost:5432/postgres")
    print(f"Using DATABASE_URL: {DATABASE_URL}")

    conn = await asyncpg.connect(DATABASE_URL)
    print("Connection successful!")
    await conn.close()

asyncio.run(test_connection())
