from fastapi import APIRouter, HTTPException
from app.models.chatbot import ChatRequest
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
router = APIRouter()



# Load the model
chatbot = pipeline("text2text-generation", model="google/flan-t5-large")


@router.post("/chat")
async def chat(request: ChatRequest):
    response = chatbot(request.query, max_length=200, do_sample=True)[0]["generated_text"]
    return {"response": response}



