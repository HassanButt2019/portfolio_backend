from app.models.contact import Contact
from app.services.db import database
from app.schemas.contact import contact_table
import uuid
from datetime import datetime
from app.utils.email import send_email


class ContactDB:
    @staticmethod
    async def create_message(contact: Contact) -> Contact:
        """Save a new contact message."""
        message_id = str(uuid.uuid4())
        current_date = datetime.utcnow()
        query = contact_table.insert().values(
            id=message_id,
            name=contact.name,
            email=contact.email,
            message=contact.message,
            linkedin=str(contact.linkedin) if contact.linkedin else None,
            github=str(contact.github) if contact.github else None,
            created_at=current_date,
        )
        await database.execute(query)
        email_subject = f"New Contact Form Submission: {contact.name}"
        email_body = (
            f"You have received a new contact form submission:\n\n"
            f"Name: {contact.name}\n"
            f"Email: {contact.email}\n"
            f"Message: {contact.message}\n"
            f"LinkedIn: {contact.linkedin or 'N/A'}\n"
            f"GitHub: {contact.github or 'N/A'}\n"
        )

        # Send email notification
        send_email(email_subject, email_body , contact.email)
        return Contact(
            id=message_id,
            name=contact.name,
            email=contact.email,
            message=contact.message,
            linkedin=contact.linkedin,
            github=contact.github,
            created_at=current_date,
        )

    @staticmethod
    async def get_all_messages() -> list[Contact]:
        """Fetch all contact messages."""
        query = contact_table.select()
        rows = await database.fetch_all(query)
        return [
            Contact(
                id=row["id"],
                name=row["name"],
                email=row["email"],
                message=row["message"],
                linkedin=row["linkedin"],
                github=row["github"],
                created_at=row["created_at"],
            )
            for row in rows
        ]
