from abc import abstractmethod
from app.domain.models.user import User
from typing import List, Optional
from app.domain.repositories.base_repo import BaseRepository

class BaseUserRepository(BaseRepository):
    @abstractmethod
    async def salvar(self, user: User):
        """
        Salva um usuário no banco de dados.
        """
        pass

    @abstractmethod
    async def get_all(self) -> List[User]:
        """
        Retorna todos os usuários.
        """
        pass

    @abstractmethod
    async def get_by_id(self, id_value: str) -> Optional[User]:
        """
        Retorna um usuário pelo seu ID.
        """
        pass

    @abstractmethod
    async def get_by_email_senha(self, email: str, senha: str) -> Optional[User]:
        """
        Retorna um usuário baseado no e-mail e senha.
        """
        pass

    @abstractmethod
    async def remove(self, id_value: str):
        """
        Remove um usuário pelo seu ID.
        """
        pass

    @abstractmethod
    async def update(self, id_value: str, user: User):
        """
        Atualiza os dados de um usuário.
        """
        pass
