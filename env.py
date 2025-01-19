# from logging.config import fileConfig

# from sqlalchemy import engine_from_config
# from sqlalchemy import pool
# from sqlalchemy.ext.asyncio import create_async_engine

# from app.schemas.database_schema import metadata  # Import your metadata

# # this is the Alembic Config object, which provides
# # access to the values within the .ini file in use.
# config = context.config

# # Interpret the config file for Python logging.
# # This line sets up loggers basically.
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)

# # add your model's MetaData object here
# # for 'autogenerate' support
# # from myapp import mymodel
# # target_metadata = mymodel.Base.metadata
# target_metadata = metadata

# # other values from the config, defined by the needs of env.py,
# # can be acquired:
# # my_important_option = config.get_main_option("my_important_option")
# # ... etc.


# def run_migrations_offline() -> None:
#     """Run migrations in 'offline' mode.

#     This configures the context with just a URL
#     and not an Engine, though an Engine is acceptable
#     here as well.  By skipping the Engine creation
#     we don't even need a DBAPI to be available.

#     Calls to context.execute() here emit the given string to the
#     script output.

#     """
#     url = config.get_main_option("sqlalchemy.url")
#     context.configure(
#         url=url,
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )

#     with context.begin_transaction():
#         context.run_migrations()

# def get_engine():
#     return create_async_engine(
#         config.get_main_option("sqlalchemy.url"),
#         poolclass=pool.NullPool,
#     )
# async def run_migrations_online():
#     connectable = get_engine()

#     async with connectable.connect() as connection:
#         await connection.run_sync(do_run_migrations)

#     await connectable.dispose()

# def do_run_migrations(connection):
#     context.configure(
#         connection=connection,
#         target_metadata=target_metadata,
#         render_as_batch=True,  # Optional: for SQLite compatibility
#     )
#     with context.begin_transaction():
#         context.run_migrations()


# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     import asyncio
#     asyncio.run(run_migrations_online())