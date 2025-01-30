from openai import OpenAI
import openai
from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv
from app.services.db import database
from app.schemas.database_schema import projects_table
from app.models.projects import Project

