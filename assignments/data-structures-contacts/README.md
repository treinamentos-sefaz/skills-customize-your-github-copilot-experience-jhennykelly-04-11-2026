# 📘 Atividade: Gerenciador de Contatos

## 🎯 Objetivo

Pratique listas e dicionários em Python criando um gerenciador de contatos que adiciona, busca, atualiza, remove e agrupa registros.

## 📝 Tarefas

### 🛠️ Adicionar Contatos

#### Descrição
Crie a função `add_contact()` que adiciona um novo contato à lista de contatos. Cada contato é um dicionário com as chaves `name`, `phone` e `email`.

#### Requisitos
O programa concluído deve:

- Receber a lista `contacts`, `name`, `phone` e `email` como parâmetros.
- Adicionar um dicionário com as chaves `name`, `phone` e `email` à lista.
- Retornar a lista atualizada.
- Exemplo de uso:

  ```python
  contacts = []
  add_contact(contacts, "Alice", "555-1234", "alice@example.com")
  print(contacts)
  # [{'name': 'Alice', 'phone': '555-1234', 'email': 'alice@example.com'}]
  ```

### 🛠️ Buscar e Listar Contatos

#### Descrição
Crie as funções `list_contacts()` e `find_contact()` para exibir todos os contatos e localizar um contato pelo nome.

#### Requisitos
O programa concluído deve:

- Implementar `list_contacts()` que imprime o nome e o telefone de cada contato, um por linha.
- Implementar `find_contact()` que recebe a lista e um nome e retorna o contato correspondente, ou `None` se não existir.
- Ignorar diferenças entre letras maiúsculas e minúsculas na busca.

### 🛠️ Atualizar e Remover Contatos

#### Descrição
Crie as funções `update_contact()` e `delete_contact()` para modificar ou excluir um contato existente.

#### Requisitos
O programa concluído deve:

- Implementar `update_contact()` que altera o telefone ou o e-mail de um contato encontrado pelo nome.
- Implementar `delete_contact()` que remove o contato encontrado pelo nome.
- Retornar `False` quando o contato não existir e `True` quando a operação for concluída.

### 🛠️ Agrupar Contatos por Inicial

#### Descrição
Crie a função `group_by_initial()` que organiza os contatos em um dicionário, usando a primeira letra do nome como chave.

#### Requisitos
O programa concluído deve:

- Retornar um dicionário em que cada chave é uma letra maiúscula e cada valor é a lista de nomes de contatos que começam com essa letra.
- Exemplo de saída para os contatos `Alice` e `Ana`:

  ```python
  {'A': ['Alice', 'Ana']}
  ```
