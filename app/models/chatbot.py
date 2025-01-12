from pydantic import BaseModel

class ChatQuery(BaseModel):
    prompt: str
