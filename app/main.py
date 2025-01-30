import asyncio
import time
from fastapi import FastAPI, Request
from starlette.responses import Response
from app.utils.logger import logger
from app.routers import contact, projects
from app.routers import chatbot
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.routers import about
from app.services.db import database
from app.routers import experience
from sqlalchemy import text
from app.config import initialize_tables
from fastapi.middleware.cors import CORSMiddleware
from app.routers import languages
from app.utils.fetch_language import fetch_repo_languages
app = FastAPI(title="Hassan Portfolio", version="1.0.0")

# @app.post("/apply-migrations")
# async def apply_migrations():
#     """Manually apply Alembic migrations."""
#     alembic_cfg = Config("alembic.ini")
#     try:
#         # Step 1: Generate migration revision
#         migrations_path = "migrations/versions/"
#         if not os.listdir(migrations_path):  # Check if the directory is empty
#             print("Generating new migration revision...")
#             command.revision(alembic_cfg, message="Create all tables", autogenerate=True)
#             print("Migration revision created successfully.")
#         else:
#             print("Migration revisions already exist.")

#         # Step 2: Apply migrations
#         print("Applying migrations...")
#         command.upgrade(alembic_cfg, "head")
#         print("Migrations applied successfully.")
#         return {"message": "Migrations generated and applied successfully."}
#     except Exception as e:
#         print(f"Migration error: {e}")
#         return {"error": str(e)}
    
@app.on_event("startup")
async def startup_event():
    """Application startup event."""
    # Ensure the database connection is established first
    await database.connect()
    await initialize_tables()
    # await fetch_repo_languages()

    logger.info("Application startup complete.")


@app.get("/health/projects")
async def check_projects_table():
    query = "SELECT 1 FROM projects LIMIT 1;"
    try:
        result = await database.fetch_one(query)
        return {"status": "healthy", "result": result}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Log request details
    start_time = time.time()
    logger.info(
        f"Request: method={request.method} path={request.url.path} client={request.client.host}"
    )
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(
        f"Response: status_code={response.status_code} "
        f"method={request.method} path={request.url.path} "
        f"process_time={process_time:.2f}s"
    )
    return response

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

app.add_middleware(
   CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend's URL
    allow_credentials=True,  # If your app uses cookies or credentials
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
# Include routes
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(chatbot.router, prefix="/api", tags=["Chatbot"])
app.include_router(about.router, prefix="/api", tags=["About Me"])
app.include_router(experience.router, prefix="/api/experience", tags=["Experience"])
app.include_router(contact.router, prefix="/api/contact", tags=["Contact"])
app.include_router(languages.router, prefix="/api/language", tags=["Language"])




@app.get("/")
def read_root():
    return {"message": "Welcome to Hassan's AI Portfolio Backend!"}



@app.get("/health")
async def health_check():
    """Health check endpoint."""
    query = "SELECT 1 FROM projects LIMIT 1;"
    try:
        result = await database.fetch_one(query)
        return {"status": "healthy", "projects_table": "exists"}
    except Exception:
        return {"status": "unhealthy", "projects_table": "does not exist"}


@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()




