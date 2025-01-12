from fastapi import APIRouter, HTTPException
from app.models.contact import Contact
from app.services.contact import ContactDB

router = APIRouter()

@router.post("/", response_model=Contact)
async def submit_contact(contact: Contact):
    """Submit a contact form message."""
    return await ContactDB.create_message(contact)

@router.get("/", response_model=list[Contact])
async def fetch_all_contacts():
    """Fetch all contact messages."""
    return await ContactDB.get_all_messages()
