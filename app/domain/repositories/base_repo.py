import asyncpg
from abc import ABC, abstractmethod
from typing import Optional, List, Any

class BaseRepository(ABC):
    def __init__(self, db: asyncpg.Connection):
        self.db = db

    @abstractmethod
    async def salvar(self, *args, **kwargs):
        pass

    @abstractmethod
    async def get_all(self, *args, **kwargs) -> List[Any]:
        pass

    @abstractmethod
    async def get_by_id(self, id_value: Any, *args, **kwargs) -> Optional[Any]:
        pass

    @abstractmethod
    async def remove(self, id_value: Any, *args, **kwargs):
        pass

    @abstractmethod
    async def update(self, id_value: Any, *args, **kwargs):
        pass
