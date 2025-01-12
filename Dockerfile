# Use a slim Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements.txt first for dependency caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Alembic configuration and migrations directory
COPY alembic.ini .
COPY migrations/ migrations/

# Copy the entire application code
COPY . .

# Expose the application port
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Add health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Wait for database to be ready and run migrations before starting the app
CMD ["sh", "-c", "if [ ! -f migrations/versions/*.py ]; then alembic revision --autogenerate -m 'Create all tables'; fi && alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
