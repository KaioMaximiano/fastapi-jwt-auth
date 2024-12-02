# FastAPI JWT Auth

## Descrição
Uma API feita com FastAPI que utiliza autenticação JWT para proteger rotas. A API interage com um banco de dados SQLite para armazenar e recuperar dados de usuários.

## Configuração

1. Clone o repositóry:
   git clone https://github.com/KaioMaximiano/fastapi-jwt-auth.git
   cd fastapi-jwt-auth

Install dependencies: 
   pip install -r requirements.txt

Configure the database and run the app:
   uvicorn app.main:app --reload
   http://127.0.0.1:8000/docs to acess SWAGGER documetation

Request in folder curl-requests.
   You can use the in Postman for example

Users
   fake_users_db = {
      "user": {"username": "user", "role": "user", "password": "L0XuwPOdS5U"},
      "admin": {"username": "admin", "role": "admin", "password": "JKSipm0YH"},
   }