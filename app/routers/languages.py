from fastapi import APIRouter, HTTPException
from app.models.projects import Project
from app.services.project import ProjectsDB
from app.schemas.database_schema import repo_languages_table
from app.services.db import database

router = APIRouter()


@router.get("/languages")
async def get_languages():
    """Fetch repository language data from the database."""
    query = repo_languages_table.select()
    rows = await database.fetch_all(query)

    if not rows:
        raise HTTPException(status_code=404, detail="No data available. Please wait for the cron job to run.")
    
    return [
        {
            "repo_name": row["repo_name"],
            "languages": row["languages"],
            "last_fetched": row["last_fetched"],
        }
        for row in rows
    ]