# Projeto Kenzie Buster

Este é um projeto semanal que tem como objetivo desenvolver um sistema com Django e Django Rest Framework (DRF) para criar um sistema de gerenciamento de usuários e filmes. Neste README, forneceremos informações sobre as rotas, solicitações e respostas do sistema, bem como as tecnologias utilizadas.

## Tecnologias Utilizadas

[![Python](https://img.shields.io/badge/python-3.11.5-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.2.6-green.svg)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/djangorestframework-3.14.0-red.svg)](https://www.django-rest-framework.org/)
[![Django Rest Framework Simple JWT](https://img.shields.io/badge/djangorestframework--simplejwt-5.3.0-yellow.svg)](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
[![IPython](https://img.shields.io/badge/ipython-8.16.1-blueviolet.svg)](https://ipython.org/)

## Estrutura do Projeto

O projeto Kenzie Buster é estruturado em várias partes. A seguir, você encontrará informações sobre as principais funcionalidades do sistema.

### User Customizado

Nesta parte do projeto, criamos um aplicativo chamado "users" com um modelo personalizado de usuário que estende o `AbstractUser` do Django. Os principais atributos do modelo incluem:

- `email`: Uma string de e-mail única com no máximo 127 caracteres.
- `first_name`: Uma string com no máximo 50 caracteres.
- `last_name`: Uma string com no máximo 50 caracteres.
- `birthdate`: Uma data (pode ser nulo e tem um valor padrão nulo).
- `is_employee`: Um booleano com valor padrão falso.

Também foram definidos dois níveis de usuário: "employee" e "usuário comum", conforme a tabela a seguir:

| Tipo de Usuário | is_superuser | is_employee |
|-----------------|--------------|-------------|
| Funcionário     | True         | True        |
| Usuário Comum   | False        | False       |

### Rotas

#### Criação de Usuário

- Rota: `POST /api/users/`
- Corpo da Requisição:
  ```json
  {
    "username": "lucira_buster",
    "email": "lucira_buster@kenziebuster.com",
    "birthdate": "1999-09-09",
    "first_name": "Lucira",
    "last_name": "Buster",
    "password": "1234",
    "is_employee": true
  }
  ```
- Resposta (Status 201 CREATED):
  ```json
  {
    "id": 1,
    "username": "lucira_buster",
    "email": "lucira_buster@kenziebuster.com",
    "first_name": "Lucira",
    "last_name": "Buster",
    "birthdate": "1999-09-09",
    "is_employee": true,
    "is_superuser": true
  }
  ```

#### Rota de Login

- Rota: `POST /api/users/login/`
- Corpo da Requisição:
  ```json
  {
    "username": "lucira_buster",
    "password": "1234"
  }
  ```
- Resposta (Status 200 OK):
  ```json
  {
    "refresh": "JWT REFRESH TOKEN...",
    "access": "JWT ACCESS TOKEN..."
  }
  ```

#### Rota de Listagem de Usuários

- Rota: `GET /api/users/`

#### Rota de Detalhes de Usuário

- Rota: `GET /api/users/<int:user_id>/`

#### Rota de Atualização de Usuário

- Rota: `PATCH /api/users/<int:user_id>/`
- Corpo da Requisição:
  ```json
  {
    "email": "lucira_updated@kenziebuster.com",
    "first_name": "Lucira Updated"
  }
  ```
- Resposta (Status 200 OK):
  ```json
  {
    "id": 1,
    "username": "lucira_buster",
    "email": "lucira_updated@kenziebuster.com",
    "first_name": "Lucira Updated",
    "last_name": "Buster",
    "birthdate": "1999-09-09",
    "is_employee": true,
    "is_superuser": true
  }
  ```

#### Rota de Exclusão de Usuário

- Rota: `DELETE /api/users/<int:user_id>/`

### Movies

Nesta parte do projeto, criamos um aplicativo chamado "movies" com um modelo "Movie" que permite que os usuários cadastrem filmes. Os atributos do modelo incluem:

- `title`: Uma string com no máximo 127 caracteres.
- `duration`: Uma string com no máximo 10 caracteres (pode ser uma string vazia).
- `rating`: Uma string com no máximo 20 caracteres, com opções "G," "PG," "PG-13," "R" ou "NC-17" (valor padrão: "G").
- `synopsis`: Uma string sem limitação de caracteres (pode ser uma string vazia).

#### Serializador de Filmes

O serializador de filmes permite a criação, listagem, atualização e exclusão de filmes. Além dos campos básicos, o atributo "added_by" retorna apenas o e-mail do usuário que cadastrou o filme.

#### Rota de Listagem de Filmes

- Rota: `GET /api/movies/`

#### Rota de Criação de Filmes

- Rota: `POST /api/movies/`
- Corpo da Requisição:
  ```json
  {
    "title": "Revolver",
    "duration": "110min",
    "rating": "R",
    "synopsis": "Jake Green is a hotshot gambler..."
  }
  ```
- Resposta (Status 201 CREATED):
  ```json
  {
    "id": 1,
    "title": "Revolver",
    "duration": "110min",
    "rating": "R",
    "synopsis": "Jake Green is a hotshot gambler...",
    "added_by": "lucira_buster@kenziebuster.com"
  }
  ```

#### Rota de Detalhes de Filmes

- Rota: `GET/api/movies/<int:movie_id>/`

#### Rota de Exclusão de Filmes

- Rota: `DELETE /api/movies/<int:movie_id>/`

#### Rota de Atualização de Filmes

- Rota: `PATCH /api/movies/<int:movie_id>/`
- Corpo da Requisição:
  ```json
  {
    "duration": "120min",
    "synopsis": "An updated synopsis."
  }
  ```
- Resposta (Status 200 OK):
  ```json
  {
    "id": 1,
    "title": "Revolver",
    "duration": "120min",
    "rating": "R",
    "synopsis": "An updated synopsis.",
    "added_by": "lucira_buster@kenziebuster.com"
  }
  ```

### Tabela Pivô Customizada

Nesta parte do projeto, criamos um aplicativo chamado "movies_orders" que contém um modelo chamado "MovieOrder." Este modelo inclui os seguintes atributos:

- `purchased_at`: Uma data e hora preenchida automaticamente pelo Django ao inserir o objeto no banco.
- `price`: Um campo Decimal com no máximo 8 dígitos e 2 casas decimais.
