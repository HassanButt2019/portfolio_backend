from sqlalchemy.dialects.postgresql import insert
from app.models.projects import Project
from app.services.db import database
from app.schemas.database_schema import projects_table
import uuid


class ProjectsDB:
    @staticmethod
    async def get_all_projects() -> list[Project]:
        """Fetch all projects."""
        query = projects_table.select()
        rows = await database.fetch_all(query)
        return [
            Project(
                id=str(row["id"]),
                title=row["title"],
                description=row["description"],
                technologies=row["technologies"].split(","),
                github_link=row["github_link"],
                live_demo_link=row["live_demo_link"],
            )
            for row in rows
        ]

    @staticmethod
    async def get_project_by_id(project_id: str) -> Project:
        """Fetch a project by ID."""
        query = projects_table.select().where(projects_table.c.id == project_id)
        row = await database.fetch_one(query)
        if row:
            return Project(
                id=row["id"],
                title=row["title"],
                description=row["description"],
                technologies=row["technologies"].split(","),
                github_link=row["github_link"],
                live_demo_link=row["live_demo_link"],
            )
        return None

    @staticmethod
    async def create_project(project: Project) -> Project:
        """Add a new project."""
        project_id = str(uuid.uuid4())  # Generate a unique ID
        query = projects_table.insert().values(
            title=project.title,
            description=project.description,
            technologies=",".join(project.technologies),
            github_link=str(project.github_link),  # Convert HttpUrl to string
            live_demo_link=str(project.live_demo_link) if project.live_demo_link else None,  # Convert HttpUrl to string or set None
        )
        await database.execute(query)
        # Create a new Project object, overriding the id field
        return Project(
            title=project.title,
            description=project.description,
            technologies=project.technologies,
            github_link=project.github_link,
            live_demo_link=project.live_demo_link,
        )

    @staticmethod
    async def update_project(project_id: str, project: Project) -> Project:
        """Update an existing project."""
        query = (
            projects_table.update()
            .where(projects_table.c.id == project_id)
            .values(
                title=project.title,
                description=project.description,
                technologies=",".join(project.technologies),
                github_link=str(project.github_link),  # Convert HttpUrl to string
                live_demo_link=str(project.live_demo_link) if project.live_demo_link else None,  # Convert HttpUrl to string or set None
            )
        )
        await database.execute(query)
        # Return the updated project with the provided project_id
        return Project(
            id=project_id,
            title=project.title,
            description=project.description,
            technologies=project.technologies,
            github_link=project.github_link,
            live_demo_link=project.live_demo_link,
        )

    @staticmethod
    async def delete_project(project_id: str):
        """Delete a project."""
        query = projects_table.delete().where(projects_table.c.id == project_id)
        await database.execute(query)
