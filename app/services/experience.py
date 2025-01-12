from sqlalchemy.dialects.postgresql import insert
from app.models.experience import Experience
from app.services.db import database
from app.schemas.experience import experience_table
import uuid


class ExperienceDB:
    @staticmethod
    async def get_all_experiences() -> list[Experience]:
        """Fetch all professional experiences."""
        query = experience_table.select()
        rows = await database.fetch_all(query)
        return [
            Experience(
                id=row["id"],
                title=row["title"],
                company=row["company"],
                start_date=row["start_date"],
                end_date=row["end_date"],
                responsibilities=row["responsibilities"].split(",") if row["responsibilities"] else [],
                technologies=row["technologies"].split(",") if row["technologies"] else [],
            )
            for row in rows
        ]

    @staticmethod
    async def get_experience_by_id(exp_id: str) -> Experience:
        """Fetch a specific experience by ID."""
        query = experience_table.select().where(experience_table.c.id == exp_id)
        row = await database.fetch_one(query)
        if row:
            return Experience(
                id=row["id"],
                title=row["title"],
                company=row["company"],
                start_date=row["start_date"],
                end_date=row["end_date"],
                responsibilities=row["responsibilities"].split(",") if row["responsibilities"] else [],
                technologies=row["technologies"].split(",") if row["technologies"] else [],
            )
        return None

    @staticmethod
    async def create_experience(exp: Experience) -> Experience:
        """Add a new professional experience."""
        exp_id = str(uuid.uuid4())  # Generate a unique ID
        query = experience_table.insert().values(
            id=exp_id,
            title=exp.title,
            company=exp.company,
            start_date=exp.start_date,
            end_date=exp.end_date,
            responsibilities=",".join(exp.responsibilities),
            technologies=",".join(exp.technologies),
        )
        await database.execute(query)

        # Fetch the newly created record to ensure consistency
        return await ExperienceDB.get_experience_by_id(exp_id)

    @staticmethod
    async def update_experience(exp_id: str, exp: Experience) -> Experience:
        """Update an existing professional experience."""
        query = (
            experience_table.update()
            .where(experience_table.c.id == exp_id)
            .values(
                title=exp.title,
                company=exp.company,
                start_date=exp.start_date,
                end_date=exp.end_date,
                responsibilities=",".join(exp.responsibilities),
                technologies=",".join(exp.technologies),
            )
        )
        await database.execute(query)

        # Fetch the updated record to ensure consistency
        return await ExperienceDB.get_experience_by_id(exp_id)

    @staticmethod
    async def delete_experience(exp_id: str):
        """Delete a professional experience."""
        query = experience_table.delete().where(experience_table.c.id == exp_id)
        await database.execute(query)
