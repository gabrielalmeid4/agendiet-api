from abc import abstractmethod
from app.domain.models.peso import Peso
from typing import List, Optional
from app.domain.repositories.base_repo import BaseRepository

class BasePesoRepository(BaseRepository):
    @abstractmethod
    async def salvar(self, peso: Peso, id_usuario: int):
        """
        Salva um registro de peso no banco de dados.
        """
        pass

    @abstractmethod
    async def get_all(self) -> List[Peso]:
        """
        Retorna todos os registros de peso.
        """
        pass

    @abstractmethod
    async def get_by_id(self, id_value: int) -> Optional[Peso]:
        """
        Retorna o peso de um usuário baseado no ID.
        """
        pass

    @abstractmethod
    async def remove(self, id_value: int):
        """
        Remove um registro de peso.
        """
        pass

    @abstractmethod
    async def update(self, id_value: int, peso: Peso):
        """
        Atualiza o registro de peso.
        """
        pass

    @abstractmethod
    async def get_latest(self, id_usuario: int) -> Optional[Peso]:
        """
        Retorna o peso mais recente de um usuário.
        """
        pass
