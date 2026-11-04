# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST em Python com o framework FastAPI, praticando rotas, parâmetros, validação de dados com Pydantic e operações CRUD.

## 📝 Tarefas

### 🛠️ Primeira Rota GET

#### Descrição
Crie a aplicação FastAPI e uma rota `GET /` que retorna uma mensagem de boas-vindas em JSON.

#### Requisitos
O programa concluído deve:

- Criar a instância `app = FastAPI()`.
- Responder a `GET /` com o JSON `{"message": "Welcome to my API"}`.
- Ser executado com `uvicorn main:app --reload` sem erros.

### 🛠️ Parâmetros de Caminho e de Consulta

#### Descrição
Crie uma rota que receba um identificador na URL e um parâmetro opcional de consulta.

#### Requisitos
O programa concluído deve:

- Implementar `GET /items/{item_id}` com `item_id` do tipo `int`.
- Aceitar o parâmetro opcional de consulta `q` do tipo `str`, com valor padrão `None`.
- Retornar um JSON com `item_id` e `q`. Exemplo:

  ```
  GET /items/5?q=caneta
  {"item_id": 5, "q": "caneta"}
  ```

### 🛠️ Modelo de Dados e Rota POST

#### Descrição
Defina um modelo Pydantic para os itens e crie uma rota que recebe e valida um item enviado pelo cliente.

#### Requisitos
O programa concluído deve:

- Criar a classe `Item` herdando de `BaseModel`, com os campos `name` (`str`), `price` (`float`) e `in_stock` (`bool`, padrão `True`).
- Implementar `POST /items` que recebe um `Item` no corpo da requisição e o retorna.
- Retornar erro de validação (código `422`) quando `price` não for um número.

### 🛠️ CRUD Completo em Memória

#### Descrição
Armazene os itens em um dicionário em memória e implemente as operações de leitura, atualização e remoção.

#### Requisitos
O programa concluído deve:

- Implementar `GET /items/{item_id}` retornando o item armazenado.
- Implementar `PUT /items/{item_id}` para substituir um item existente.
- Implementar `DELETE /items/{item_id}` para remover um item.
- Retornar código `404` com a mensagem `"Item not found"` quando o item não existir.
