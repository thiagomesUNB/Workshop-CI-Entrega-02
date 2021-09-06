import pathlib
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

sys.path.append(str(pathlib.Path(__file__).resolve().parents[3]))

from app.core.config import DATABASE_URL  # isort:skip

config = context.config

fileConfig(config.config_file_name)

target_metadata = None

config.set_main_option("sqlalchemy.url", str(DATABASE_URL))


def run_migrations_online() -> None:
    print('aaa')
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    print('bbb')

    with connectable.connect() as connection:
        print('ccc')
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            print('ddd')
            context.run_migrations()
            print('eee')


run_migrations_online()
