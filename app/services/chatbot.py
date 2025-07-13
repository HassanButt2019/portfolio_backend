import re
import fitz
from openai import OpenAI
import openai
from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv
from app.services.db import database
from app.schemas.database_schema import projects_table
from app.models.projects import Project
from pathlib import Path

from openai import OpenAI
import chromadb

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="resumes")

# You can call this at startup or when adding new resumes
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def ingest_resumes_from_pdfs():
    folder_path = Path("app") / "data"
    files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
    for idx, file in enumerate(files):
        path = os.path.join(folder_path, file)
        text = extract_text_from_pdf(path)
        embedding = client.embeddings.create(
            model="text-embedding-3-large",
            input=text
        ).data[0].embedding
        collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[f"resume-{idx}"]
        )
import json

def ask_resume_chat(question: str):
    # Create embedding for the question
    q_embedding = client.embeddings.create(
        model="text-embedding-3-large",
        input=question
    ).data[0].embedding

    # Query Chroma (top-1)
    results = collection.query(
        query_embeddings=[q_embedding],
        n_results=1
    )

    # Safety check: no docs found
    if not results['documents'] or not results['documents'][0]:
        return {
            "answer": "Hassan doesn't know about it.",
            "follow_ups": []
        }

    top_score = results['distances'][0][0]
    top_text = results['documents'][0][0]

    if top_score < 2.0:
        prompt = f"""
You are Hassan's professional portfolio assistant.

Use ONLY the information provided in the context below to answer the question about Hassan's professional experience.

When answering:
- If possible, include specific projects, companies, or roles mentioned in the context that are relevant to the question.
- If asked about Hassan's availability for work, simply reply: "Yes, we can talk about it."
- If the context does not have enough information, or if the question is not related to Hassan's professional experience, set the "answer" field to: "Hassan doesn't know about it."

Then, provide 2-3 follow-up questions related to the context.

Return your response strictly as a JSON object WITHOUT any markdown, triple backticks, or code block formatting. Only output valid JSON like this:
{{
    "answer": "...",
    "follow_up_questions": ["...", "..."]
}}

Context:
\"\"\"
{top_text}
\"\"\"

Question:
\"{question}\"
"""

        # Call OpenAI completion
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )

        raw_content = response.choices[0].message.content

        # Remove ```json or ``` if model still adds them
        cleaned_content = re.sub(r"```(json)?", "", raw_content).strip()

        try:
            data = json.loads(cleaned_content)
            answer = data.get("answer", "Hassan doesn't know about it.")
            follow_ups = data.get("follow_up_questions", [])
            return {
                "answer": answer,
                "follow_ups": follow_ups
            }
        except json.JSONDecodeError:
            return {
                "answer": raw_content,
                "follow_ups": []
            }

    else:
        return {
            "answer": "Hassan doesn't know about it.",
            "follow_ups": []
        }