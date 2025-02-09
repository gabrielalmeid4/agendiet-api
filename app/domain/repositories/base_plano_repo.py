from abc import abstractmethod
from app.domain.models.plano_alimentar import PlanoAlimentar
from typing import List, Optional
from app.domain.repositories.base_repo import BaseRepository

class BasePlanoAlimentarRepository(BaseRepository):
    @abstractmethod
    async def salvar(self, plano_alimentar: PlanoAlimentar, id_usuario: int):
        """
        Salva um plano alimentar no banco de dados.
        """
        pass

    @abstractmethod
    async def get_all(self) -> List[PlanoAlimentar]:
        """
        Retorna todos os planos alimentares.
        """
        pass

    @abstractmethod
    async def get_by_id(self, id_value: int) -> Optional[PlanoAlimentar]:
        """
        Retorna um plano alimentar baseado no ID.
        """
        pass

    @abstractmethod
    async def remove(self, id_value: int):
        """
        Remove um plano alimentar.
        """
        pass

    @abstractmethod
    async def update(self, id_value: int, plano_alimentar: PlanoAlimentar):
        """
        Atualiza um plano alimentar.
        """
        pass
