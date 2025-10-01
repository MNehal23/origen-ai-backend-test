# part_a/app/db/database.py
import asyncio
import asyncpg
import os
from pathlib import Path

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/origen")

DDL_PATH = Path(__file__).parent / "ddl.sql"
MACHINE_FIXTURES = [
    ("m-1.large", "GPU machine type 1"),
    ("m-2.xlarge", "GPU machine type 2"),
    ("cpu.medium", "CPU machine example"),
]

async def _execute_ddl(conn):
    ddl = DDL_PATH.read_text()
    await conn.execute(ddl)

async def _seed_machines(conn):
    for name, desc in MACHINE_FIXTURES:
        await conn.execute("""
            INSERT INTO machine(name, description) VALUES ($1, $2)
            ON CONFLICT (name) DO NOTHING
        """, name, desc)

async def init_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        await _execute_ddl(conn)
        await _seed_machines(conn)
    finally:
        await conn.close()

def run_init_db():
    asyncio.get_event_loop().run_until_complete(init_db())
