# Código Inicial para a Tarefa de APIs REST com FastAPI
# Instale as dependências com: pip install fastapi uvicorn
# Renomeie este arquivo para main.py e execute com: uvicorn main:app --reload

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# TODO: Criar a rota GET / que retorna {"message": "Welcome to my API"}


# TODO: Criar a rota GET /items/{item_id} com o parâmetro de consulta opcional q


# TODO: Criar a classe Item (name, price, in_stock) herdando de BaseModel
# class Item(BaseModel):
#     ...


# TODO: Criar a rota POST /items que recebe um Item


# TODO: Criar um dicionário em memória e as rotas PUT e DELETE /items/{item_id}
# items = {}
