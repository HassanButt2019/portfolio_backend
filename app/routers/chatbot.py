from fastapi import APIRouter, HTTPException
from app.models.chatbot import ChatRequest
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

from app.services.chatbot import ask_resume_chat
router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    answer = ask_resume_chat(request.query)
    return answer
