# AgenDiet API

Uma API feita utilizando o framework FastAPI da linguagem Python, como backend para ser consumido pela seguinte aplicação Flutter: [AgenDiet](https://github.com/marianaandrxde/agendiet).

# **Como rodar**

1. **Clonar o projeto.**  
2. **Criar máquina virtual com Python versão 3.11**, baixando as dependências do `requirements.txt`.  
3. **Criar um `.env` na raiz do projeto** com os dados do banco.  
4. **Rodar servidor com o comando:**  
   ```bash
   python -m uvicorn main:app --reload

5. **Acessar a rota http://localhost:8000/docs para ver a documentação Swagger da API, com as rotas disponíveis e o que elas esperam como Body da requisição ou na URL.**

# English Ver.:

# AgenDiet API

An API built using the FastAPI framework in Python as the backend for the following Flutter application: [AgenDiet](https://github.com/marianaandrxde/agendiet).

# **How to Run**

1. **Clone the project.**  
2. **Create a virtual environment with Python version 3.11** and install dependencies from `requirements.txt`.  
3. **Create a `.env` file in the project's root directory** with the database credentials.  
4. **Run the server using the following command:**  
   ```bash
   python -m uvicorn main:app --reload
