DO $$
BEGIN
    -- Check if the 'projects' table exists
    IF NOT EXISTS (
        SELECT FROM information_schema.tables
        WHERE table_schema = 'public'
        AND table_name = 'projects'
    ) THEN
        -- Create the 'projects' table
        CREATE TABLE projects (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            technologies TEXT,
            github_link VARCHAR(255) NOT NULL,
            live_demo_link VARCHAR(255)
        );
        RAISE NOTICE 'Table "projects" created successfully.';
    ELSE
        RAISE NOTICE 'Table "projects" already exists.';
    END IF;
END $$;
