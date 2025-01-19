from typing import List, Optional
from sqlalchemy.dialects.postgresql import insert
from app.models.projects import Project
from app.services.db import database
from app.schemas.database_schema import projects_table
import uuid
from datetime import datetime


class ProjectsDB:
    @staticmethod
    async def get_all_projects() -> List[Project]:
        """Fetch all projects."""
        query = projects_table.select()
        rows = await database.fetch_all(query)

        projects = []
        for row in rows:
            try:
                # Create a Project object for each row, skipping invalid rows
                projects.append(
                    Project(
                        id=row["id"],
                        title=row["title"],
                        description=row["description"],
                        short_description=row["short_description"],
                        category=row["category"],
                        status=row["status"],
                        priority=row["priority"],
                        start_date=row["start_date"],
                        end_date=row["end_date"],
                        last_updated=row["last_updated"],
                        technologies=row["technologies"],
                        architecture=row["architecture"],
                        deployment=row["deployment"],
                        repository=row["repository"],
                        team=row["team"],
                        collaborators=row["collaborators"],
                        progress=row["progress"],
                        metrics=row["metrics"],
                        milestones=row["milestones"],
                        tasks=row["tasks"],
                        images=row["images"],
                        documentation=row["documentation"],
                        links=row["links"],
                    )
                )
            except KeyError as e:
                print(f"Missing field {e} in row: {row}")
            except Exception as e:
                print(f"Error processing row {row}: {e}")

        return projects

    @staticmethod
    async def get_project_by_id(project_id: int) -> Optional[Project]:
        """Fetch a project by ID."""
        query = projects_table.select().where(projects_table.c.id == project_id)
        row = await database.fetch_one(query)
        if row:
            return Project(
                id=row["id"],
                title=row["title"],
                description=row["description"],
                short_description=row["short_description"],
                category=row["category"],
                status=row["status"],
                priority=row["priority"],
                start_date=row["start_date"],
                end_date=row["end_date"],
                last_updated=row["last_updated"],
                # Directly use the JSONB array
                technologies=row["technologies"],
                architecture=row["architecture"],
                deployment=row["deployment"],
                repository=row["repository"],
                team=row["team"],  # Directly use the JSONB array
                # Directly use the JSONB array
                collaborators=row["collaborators"],
                progress=row["progress"],
                metrics=row["metrics"],
                milestones=row["milestones"],
                tasks=row["tasks"],
                images=row["images"],
                documentation=row["documentation"],
                links=row["links"],
            )
        return None

    @staticmethod
    async def create_project(project: Project) -> Project:
        """Add a new project."""
        # Generate a unique ID
        # Convert UUID to a smaller integer
        project_id = int(uuid.uuid4().int % (10**9))
        # Insert project into the database
        query = projects_table.insert().values(
            id=project_id,
            title=project.title,
            description=project.description,
            short_description=project.short_description,
            category=project.category,
            status=project.status,
            priority=project.priority,
            start_date=datetime.utcnow(),
            end_date=project.end_date,
            last_updated=datetime.utcnow(),  # Automatically set last_updated to current time
            technologies=project.technologies,
            architecture=project.architecture,
            deployment=project.deployment,
            repository=project.repository,
            team=project.team,
            collaborators=project.collaborators,
            progress=project.progress,
            metrics=project.metrics,
            milestones=project.milestones,
            tasks=project.tasks,
            images=project.images,
            documentation=project.documentation,
            links=project.links,
        )
        await database.execute(query)

        # Create and return a new Project object
        return Project(
            id=project_id,
            title=project.title,
            description=project.description,
            short_description=project.short_description,
            category=project.category,
            status=project.status,
            priority=project.priority,
            start_date=project.start_date,
            end_date=project.end_date,
            last_updated=datetime.utcnow(),
            technologies=project.technologies,
            architecture=project.architecture,
            deployment=project.deployment,
            repository=project.repository,
            team=project.team,
            collaborators=project.collaborators,
            progress=project.progress,
            metrics=project.metrics,
            milestones=project.milestones,
            tasks=project.tasks,
            images=project.images,
            documentation=project.documentation,
            links=project.links,
        )

    @staticmethod
    async def update_project(project_id: int, project: Project) -> Project:
        """Update an existing project."""
        query = (
            projects_table.update()
            .where(projects_table.c.id == project_id)
            .values(
                title=project.title,
                description=project.description,
                short_description=project.short_description,
                category=project.category,
                status=project.status,
                priority=project.priority,
                start_date=project.start_date,
                end_date=project.end_date,
                technologies=project.technologies,
                architecture=project.architecture,
                deployment=project.deployment,
                repository=project.repository,
                team=project.team,
                collaborators=project.collaborators,
                progress=project.progress,
                metrics=project.metrics,
                milestones=project.milestones,
                tasks=project.tasks,
                images=project.images,
                documentation=project.documentation,
                links=project.links,
            )
        )
        await database.execute(query)

        # Return the updated project with the provided project_id
        return Project(
            id=project_id,
            title=project.title,
            description=project.description,
            short_description=project.short_description,
            category=project.category,
            status=project.status,
            priority=project.priority,
            start_date=project.start_date,
            end_date=project.end_date,
            last_updated="NOW()",  # Reflect the updated timestamp
            technologies=project.technologies,
            architecture=project.architecture,
            deployment=project.deployment,
            repository=project.repository,
            team=project.team,
            collaborators=project.collaborators,
            progress=project.progress,
            metrics=project.metrics,
            milestones=project.milestones,
            tasks=project.tasks,
            images=project.images,
            documentation=project.documentation,
            links=project.links,
        )

    @staticmethod
    async def delete_project(project_id: str):
        """Delete a project."""
        query = projects_table.delete().where(projects_table.c.id == project_id)
        await database.execute(query)
