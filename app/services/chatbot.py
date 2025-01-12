from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_chatbot_response(prompt: str) -> str:
    try:
        # Use the ChatCompletion endpoint
        response = client.chat.completions.create(model="gpt-3.5-turbo",  # Use "gpt-4" for GPT-4 if needed
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150)
        # Extract and return the response text
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"
