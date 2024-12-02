# FastAPI JWT Auth

## Description
The API that uses FastAPI with auth JWT to protect routes. The API interacts with the SQLite database to store and retrieve user's data

## Set up and Configuration

Clone o repositóry:
   git clone https://github.com/KaioMaximiano/fastapi-jwt-auth.git
   cd fastapi-jwt-auth

Install dependencies: 
   pip install -r requirements.txt

Configure the database and run the app:
   uvicorn app.main:app --reload
   http://127.0.0.1:8000/docs to access SWAGGER documentation

Example requests in folder app/curl-requests.
   You can use the in the Postman for example

Users
   fake_users_db = {
      "user": {"username": "user", "role": "user", "password": "L0XuwPOdS5U"},
      "admin": {"username": "admin", "role": "admin", "password": "JKSipm0YH"},
   }
