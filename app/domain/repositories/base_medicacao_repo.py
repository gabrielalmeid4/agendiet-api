from abc import abstractmethod
from app.domain.models.medicacao import Medicacao
from typing import List, Optional
from app.domain.repositories.base_repo import BaseRepository

class BaseMedicacaoRepository(BaseRepository):
    @abstractmethod
    async def salvar(self, medicacao: Medicacao, id_usuario: int):
        """
        Salva uma medicação no banco de dados.
        """
        pass

    @abstractmethod
    async def get_all(self) -> List[Medicacao]:
        """
        Retorna todas as medicações.
        """
        pass

    @abstractmethod
    async def get_by_id(self, id_value: int) -> Optional[Medicacao]:
        """
        Retorna uma medicação pelo ID.
        """
        pass

    @abstractmethod
    async def remove(self, id_value: int):
        """
        Remove uma medicação.
        """
        pass

    @abstractmethod
    async def update(self, id_value: int, medicacao: Medicacao):
        """
        Atualiza uma medicação.
        """
        pass