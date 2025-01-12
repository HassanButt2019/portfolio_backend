from app.services.db import database
from app.schemas.database_schema import about_me_table
from app.models.about import AboutMe
from sqlalchemy.dialects.postgresql import insert

class AboutMeDB:
    @staticmethod
    async def get_about_me() -> AboutMe:
        """Fetch the 'About Me' entry."""
        query = about_me_table.select()
        row = await database.fetch_one(query)
        if row:
            return AboutMe(
                id=row["id"],
                name=row["name"],
                bio=row["bio"],
                skills=row["skills"].split(","),
            )
        return None

    @staticmethod
    async def update_about_me(about_data: AboutMe) -> AboutMe:
        """Insert or update the 'About Me' entry."""
        # Use PostgreSQL's insert with ON CONFLICT
        query = insert(about_me_table).values(
            id=about_data.id,
            name=about_data.name,
            bio=about_data.bio,
            skills=",".join(about_data.skills),
        ).on_conflict_do_update(
            index_elements=["id"],
            set_={
                "name": about_data.name,
                "bio": about_data.bio,
                "skills": ",".join(about_data.skills),
            },
        )
        await database.execute(query)
        return about_data