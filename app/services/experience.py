from typing import Optional
from sqlalchemy.dialects.postgresql import insert
from app.models.experience import Experience, Company, Location
from app.services.db import database
from app.schemas.database_schema import experience_table
import uuid


class ExperienceDB:
    @staticmethod
    async def get_all_experiences() -> list[Experience]:
        """Fetch all professional experiences."""
        query = experience_table.select()
        rows = await database.fetch_all(query)
        print(rows[0]._mapping if rows else "No data found.")

        experiences = []
        for row in rows:
            # Parse the company and location JSON data
            company_data = row["company"]
            company = Company(
                id=company_data.get("id"),
                name=company_data.get("name"),
                logo=company_data.get("logo"),
                industry=company_data.get("industry"),
                website=company_data.get("website"),
                size=company_data.get("size"),
                location=Location(
                    city=company_data.get("city"),
                    country=company_data.get("country"),
                    remote=company_data.get("remote")
                ) if company_data.get("location") is None else Location(
                    city=company_data["location"].get("city"),
                    country=company_data["location"].get("country"),
                    remote=company_data["location"].get("remote")
                )
            )

            # Parse the location JSON data
            location_data = row["location"]
            location = None
            if location_data:
                location = Location(
                    city=location_data.get("city"),
                    country=location_data.get("country"),
                    remote=location_data.get("remote")
                )

            # Parse responsibilities and technologies JSON data
            responsibilities = row["responsibilities"] or []
            technologies = row["technologies"] or []

            # Build the Experience object
            experiences.append(
                Experience(
                    id=row["id"],
                    title=row["title"],
                    company=company,
                    type=row["type"],
                    location=location,
                    start_date=row["start_date"],
                    end_date=row["end_date"],
                    current=row["current"] == "true",
                    description=row["description"],
                    responsibilities=responsibilities,
                    technologies=technologies,
                )
            )

        return experiences

    @staticmethod
    async def get_experience_by_id(exp_id: int) -> Optional[Experience]:
        """
        Fetch a specific experience by ID.

        Args:
            exp_id (int): The ID of the experience to fetch.

        Returns:
            Optional[Experience]: The Experience object if found, otherwise None.
        """
        try:
            query = experience_table.select().where(experience_table.c.id == exp_id)
            row = await database.fetch_one(query)

            if not row:
                # Log the absence of the experience
                print(f"Experience with ID {exp_id} not found.")
                return None

            # Parse the company JSON data
            company_data = row.get("company", {})
            company = Company(
                id=company_data.get("id"),
                name=company_data.get("name"),
                logo=company_data.get("logo"),
                industry=company_data.get("industry"),
                website=company_data.get("website"),
                size=company_data.get("size"),
                location=Location(
                    city=company_data.get("location", {}).get("city"),
                    country=company_data.get("location", {}).get("country"),
                    remote=company_data.get("location", {}).get("remote", True),
                ) if company_data.get("location") else None,
            )

            # Parse the location JSON data
            location_data = row.get("location", {})
            location = Location(
                city=location_data.get("city"),
                country=location_data.get("country"),
                remote=location_data.get("remote", False),
            ) if location_data else None

            # Parse responsibilities and technologies JSON data
            responsibilities = row.get("responsibilities", [])
            technologies = row.get("technologies", [])

            # Build and return the Experience object
            return Experience(
                id=row["id"],
                title=row["title"],
                company=company,
                type=row["type"],
                location=location,
                start_date=row["start_date"],
                end_date=row["end_date"],
                current=row["current"] == "true",
                description=row["description"],
                responsibilities=responsibilities,
                technologies=technologies,
            )

        except Exception as e:
            # Log the exception for debugging
            print(f"Error fetching experience with ID {exp_id}: {e}")
            return None

    @staticmethod
    async def create_experience(exp: Experience) -> Experience:
        """
        Add a new professional experience to the database.

        Args:
            exp (Experience): The Experience object to be added.

        Returns:
            Experience: The created Experience object.
        """
        try:
            # Generate a unique ID for the experience
            exp_id = int(uuid.uuid4().int % (10**9))

            # Construct the company JSON data
            company_data = {
                "id": exp.company.id,
                "name": exp.company.name,
                "logo": exp.company.logo,
                "industry": exp.company.industry,
                "website": exp.company.website,
                "size": exp.company.size,
                "location": {
                    "city": exp.company.location.city if exp.company.location else None,
                    "country": exp.company.location.country if exp.company.location else None,
                    "remote": exp.company.location.remote if exp.company.location else True,
                } if exp.company.location else None,
            }

            # Construct the location JSON data (if provided)
            location_data = {
                "city": exp.location.city if exp.location else None,
                "country": exp.location.country if exp.location else None,
                "remote": exp.location.remote if exp.location else False,
            } if exp.location else None

            # Insert the new experience into the database
            query = experience_table.insert().values(
                id=exp_id,
                title=exp.title,
                description=exp.description,
                company=company_data,  # JSON data for the company
                location=location_data,  # JSON data for the location
                type=exp.type,
                current= True if exp.current else False ,  # Store as a string
                start_date=exp.start_date,
                end_date=exp.end_date,
                responsibilities=exp.responsibilities or [],  # Use an empty list if None
                technologies=exp.technologies or [],  # Use an empty list if None
            )
            await database.execute(query)

            # Log the successful creation
            print(f"Experience with ID {exp_id} created successfully.")

            # Return the created Experience object
            return exp

        except Exception as e:
            # Log the exception for debugging
            print(f"Error creating experience: {e}")
            raise

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
