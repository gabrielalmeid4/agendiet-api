from abc import abstractmethod
from app.domain.models.nutricionista import Nutricionista
from typing import List, Optional
from app.domain.repositories.base_repo import BaseRepository

class BaseNutricionistaRepository(BaseRepository):
    @abstractmethod
    async def salvar(self, nutricionista: Nutricionista):
        """
        Salva um nutricionista no banco de dados.
        """
        pass

    @abstractmethod
    async def get_all(self) -> List[Nutricionista]:
        """
        Retorna todos os nutricionistas.
        """
        pass

    @abstractmethod
    async def get_by_id(self, id_value: int) -> Optional[Nutricionista]:
        """
        Retorna um nutricionista baseado no ID.
        """
        pass

    @abstractmethod
    async def remove(self, id_value: int):
        """
        Remove um nutricionista.
        """
        pass

    @abstractmethod
    async def update(self, id_value: int, nutricionista: Nutricionista):
        """
        Atualiza um nutricionista.
        """
        pass
