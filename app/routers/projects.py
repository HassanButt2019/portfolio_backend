from fastapi import APIRouter, HTTPException
from app.models.projects import Project
from app.services.project import ProjectsDB

router = APIRouter()

@router.get("/", response_model=list[Project])
async def fetch_projects():
    """Fetch all projects."""
    return await ProjectsDB.get_all_projects()

@router.get("/{project_id}", response_model=Project)
async def fetch_project(project_id: int):
    """Fetch a project by ID."""
    project = await ProjectsDB.get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("/", response_model=Project)
async def create_project(project: Project):
    """Create a new project."""
    return await ProjectsDB.create_project(project)

# @router.put("/{project_id}", response_model=Project)
# async def update_project(project_id: int, project: Project):
#     """Update an existing project."""
#     existing_project = await ProjectsDB.get_project_by_id(project_id)
#     if not existing_project:
#         raise HTTPException(status_code=404, detail="Project not found")
#     return await ProjectsDB.update_project(project_id, project)

@router.delete("/{project_id}")
async def delete_project(project_id: int):
    """Delete a project."""
    existing_project = await ProjectsDB.get_project_by_id(project_id)
    if not existing_project:
        raise HTTPException(status_code=404, detail="Project not found")
    await ProjectsDB.delete_project(project_id)
    return {"detail": "Project deleted successfully"}
