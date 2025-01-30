from fastapi import APIRouter, HTTPException
from app.models.experience import Experience
from app.services.experience import ExperienceDB

router = APIRouter()

@router.get("/", response_model=list[Experience])
async def fetch_experiences():
    """Fetch all professional experiences."""
    return await ExperienceDB.get_all_experiences()

@router.get("/{exp_id}", response_model=Experience)
async def fetch_experience(exp_id: int):
    """Fetch a specific professional experience by ID."""
    experience = await ExperienceDB.get_experience_by_id(exp_id)
    if not experience:
        raise HTTPException(status_code=404, detail="Experience not found")
    return experience

@router.post("/", response_model=Experience)
async def create_experience(experience: Experience):
    """Create a new professional experience."""
    return await ExperienceDB.create_experience(experience)

# @router.put("/{exp_id}", response_model=Experience)
# async def update_experience(exp_id: int, experience: Experience):
#     """Update an existing professional experience."""
#     existing_experience = await ExperienceDB.get_experience_by_id(exp_id)
#     if not existing_experience:
#         raise HTTPException(status_code=404, detail="Experience not found")
#     return await ExperienceDB.update_experience(exp_id, experience)

@router.delete("/{exp_id}")
async def delete_experience(exp_id: int):
    """Delete a professional experience."""
    existing_experience = await ExperienceDB.get_experience_by_id(exp_id)
    if not existing_experience:
        raise HTTPException(status_code=404, detail="Experience not found")
    await ExperienceDB.delete_experience(exp_id)
    return {"detail": "Experience deleted successfully"}
