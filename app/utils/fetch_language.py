import httpx
from app.services.db import database
from app.schemas.database_schema import repo_languages_table
import os
from dotenv import load_dotenv
from sqlalchemy import func
import uuid

load_dotenv()

# GitHub Personal Access Token (ensure repo scope is enabled)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com"
OWNER = "HassanButt2019"  # Replace with your GitHub username

async def fetch_repo_languages():
    """Fetch languages for all repositories and save to DB."""
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

    # Step 1: Fetch repositories
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{GITHUB_API_URL}/users/{OWNER}/repos", headers=headers)
        response.raise_for_status()
        repos = response.json()

        for repo in repos:
            repo_name = repo["name"]
            languages_url = repo["languages_url"]

            # Step 2: Fetch language stats for each repository
            lang_response = await client.get(languages_url, headers=headers)
            lang_response.raise_for_status()
            languages = lang_response.json()
            project_id = int(uuid.uuid4().int % (10**9))
            # Step 3: Save to database
            query = repo_languages_table.insert().values(
                id=project_id,
                repo_name=repo_name,
                languages=languages,
                last_fetched=func.now(),
            )
            await database.execute(query)
    print("Repository languages updated.")

# Run the function (use in a cron job or scheduler)
# import asyncio
# asyncio.run(fetch_repo_languages())
