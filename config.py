import os
import asyncpg
from dotenv import load_dotenv
import ssl

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

async def get_db():
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = True
    ssl_context.verify_mode = ssl.CERT_REQUIRED

    conn = await asyncpg.connect(
        host=DB_HOST,
        port=5432,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        ssl=ssl_context     
    )
    try:
        yield conn
    finally:
        await conn.close()
