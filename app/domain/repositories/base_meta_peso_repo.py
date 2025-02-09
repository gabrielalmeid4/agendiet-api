from abc import abstractmethod
from app.domain.models.meta_peso import MetaPeso
from typing import List, Optional
from app.domain.repositories.base_repo import BaseRepository

class BaseMetaPesoRepository(BaseRepository):
    @abstractmethod
    async def salvar(self, meta_peso: MetaPeso, id_usuario: int):
        """
        Salva uma meta de peso no banco de dados.
        """
        pass

    @abstractmethod
    async def get_all(self) -> List[MetaPeso]:
        """
        Retorna todas as metas de peso.
        """
        pass

    @abstractmethod
    async def get_by_id(self, id_value: int) -> Optional[MetaPeso]:
        """
        Retorna uma meta de peso baseado no ID.
        """
        pass

    @abstractmethod
    async def remove(self, id_value: int):
        """
        Remove uma meta de peso.
        """
        pass

    @abstractmethod
    async def update(self, id_value: int, meta_peso: MetaPeso):
        """
        Atualiza uma meta de peso.
        """
        pass