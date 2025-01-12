from fastapi import APIRouter, HTTPException
from app.services.chatbot import get_chatbot_response

router = APIRouter()

@router.post("/chatbot")
def ask_chatbot(prompt: str):
    response = get_chatbot_response(prompt)
    if "Error" in response:
        raise HTTPException(status_code=500, detail=response)
    return {"response": response}
