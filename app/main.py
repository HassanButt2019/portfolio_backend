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


app = FastAPI(title="Hassan Portfolio", version="1.0.0")
@app.on_event("startup")
async def startup_event():
    await database.connect()
    logger.info("Application startup complete.")

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
# Include routes
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(chatbot.router, prefix="/api", tags=["Chatbot"])
app.include_router(about.router, prefix="/api", tags=["About Me"])
app.include_router(experience.router, prefix="/api/experience", tags=["Experience"])
app.include_router(contact.router, prefix="/api/contact", tags=["Contact"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Hassan's AI Portfolio Backend!"}


@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()
