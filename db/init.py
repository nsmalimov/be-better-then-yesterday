import asyncpg
from db.db import DB

async def connect(user, password, database, host):
    conn = await asyncpg.connect(user=user, password=password,
                                 database=database, host=host)

    return DB(conn)
