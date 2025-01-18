import asyncpg

class BaseRepository:
    def __init__(self, db: asyncpg.Connection):
        self.db = db    


