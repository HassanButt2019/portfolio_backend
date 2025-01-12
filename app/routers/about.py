from fastapi import APIRouter, HTTPException
from app.models.about import AboutMe
from app.services.about import AboutMeDB

router = APIRouter()

@router.get("/", response_model=AboutMe)
async def fetch_about_me():
    """Fetch the 'About Me' entry."""
    about = await AboutMeDB.get_about_me()
    if not about:
        raise HTTPException(status_code=404, detail="About Me data not found.")
    return about

@router.put("/", response_model=AboutMe)
async def modify_about_me(about_data: AboutMe):
    """Update the 'About Me' entry."""
    updated_about = await AboutMeDB.update_about_me(about_data)
    return updated_about
