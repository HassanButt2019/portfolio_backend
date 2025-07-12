# Portfolio Backend

This project contains a simple FastAPI application backed by a PostgreSQL
database.  Alembic has been removed; tables are created on startup using SQL
statements defined in `app/config.py`.

## Running Locally

1. **Install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Set up PostgreSQL**

   - Ensure a PostgreSQL server is running on `localhost:5432`.
   - Create a database named `portfolio` and user `postgres` with password
     `1234` (or adjust the `DATABASE_URL` accordingly).
   - The provided `init.sql` file is executed when using `docker-compose`, but
     you can run it manually to create the `projects` table.

3. **Configure environment variables**

   The application expects `DATABASE_URL` to point to your database, for
   example:

   ```bash
   export DATABASE_URL="postgresql+asyncpg://postgres:1234@localhost:5432/portfolio"
   ```

4. **Start the server**

   ```bash
   uvicorn app.main:app --reload
   ```

Alternatively you can use Docker Compose which will start PostgreSQL and the
application together:

```bash
docker-compose up --build
```
 
