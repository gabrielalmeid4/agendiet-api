**Tutorial :)**

1 - Clonar o projeto.
2 - Criar máquina virtual com python versão 3.11 baixando as dependências do requirements.txt.
3 - Criar um .env na raiz do projeto com os dados do banco.
4 - Rodar comando:
**python -m uvicorn main:app --reload**
Para rodar o servidor, que vai escutar requisições na porta 8000.
5 - Acessar o http://localhost:8000/docs para ver a documentação Swagger da API, com as rotas disponíveis e o que elas esperam como Body da requisição ou na URL.
6 - Favor não utilizar a API em aplicações Flutter e Dart (não gosto desse framework nem dessa linguagem).
