# Kenzie Buster Project

This is a weekly project aimed at developing a system using Django and Django Rest Framework (DRF) to create a user and movie management system. In this README, we provide information about the system's routes, requests, and responses, as well as the technologies used.

## Technologies Used

[![Python](https://img.shields.io/badge/python-3.11.5-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.2.6-green.svg)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/djangorestframework-3.14.0-red.svg)](https://www.django-rest-framework.org/)
[![Django Rest Framework Simple JWT](https://img.shields.io/badge/djangorestframework--simplejwt-5.3.0-yellow.svg)](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
[![IPython](https://img.shields.io/badge/ipython-8.16.1-blueviolet.svg)](https://ipython.org/)

## Project Structure

The Kenzie Buster project is structured into several parts. Below, you will find information about the system's main functionalities.

### Custom User

In this part of the project, we created an app called "users" with a custom user model that extends Django's `AbstractUser`. The model's key attributes include:

- `email`: A unique email string with a maximum of 127 characters.
- `first_name`: A string with a maximum of 50 characters.
- `last_name`: A string with a maximum of 50 characters.
- `birthdate`: A date (can be null and has a default value of null).
- `is_employee`: A boolean with a default value of false.

Two user levels were also defined: "employee" and "common user," as shown in the table below:

| User Type       | is_superuser | is_employee |
|-----------------|--------------|-------------|
| Employee        | True         | True        |
| Common User     | False        | False       |


### Routes

#### User Creation

- Route: `POST /api/users/`
- Request Body:
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
- Response (Status 201 CREATED):
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

#### Login Route

- Route: `POST /api/users/login/`
- Request Body:
  ```json
  {
    "username": "lucira_buster",
    "password": "1234"
  }
  ```
- Response (Status 200 CREATED):
  ```json
  {
    "refresh": "JWT REFRESH TOKEN...",
    "access": "JWT ACCESS TOKEN..."
  }
  ```

#### User Listing Route

- Route: `GET /api/users/`

#### User Details Route

- Route: `GET /api/users/<int:user_id>/`

#### User Update Route

- Route: `PATCH /api/users/<int:user_id>/`
- Request Body:
  ```json
  {
    "email": "lucira_updated@kenziebuster.com",
    "first_name": "Lucira Updated"
  }
  ```
- Response (Status 200 OK):
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

#### User Deletion Route

- Route: `DELETE /api/users/<int:user_id>/`

### Movies

In this part of the project, we created an app called "movies" with a "Movie" model that allows users to register movies. The model's attributes include:

- `title`: A string with a maximum of 127 characters.
- `duration`: A string with a maximum of 10 characters (can be an empty string).
- `rating`: A string with a maximum of 20 characters, with options "G," "PG," "PG-13," "R," or "NC-17" (default value: "G").
- `synopsis`: A string with no character limit (can be an empty string).

#### Movie Serializer

The movie serializer allows the creation, listing, updating, and deletion of movies. In addition to the basic fields, the "added_by" attribute returns only the email of the user who registered the movie.

#### Movie Listing Route

- Route: `GET /api/movies/`

#### Movie Creation Route

- Route: `POST /api/movies/`
- Request Body:
  ```json
  {
    "title": "Revolver",
    "duration": "110min",
    "rating": "R",
    "synopsis": "Jake Green is a hotshot gambler..."
  }
  ```
- Response (Status 201 CREATED):
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

#### Movie Details Route

- Route: `GET /api/movies/<int:movie_id>/`

#### Movie Deletion Route

- Route: `DELETE /api/movies/<int:movie_id>/`

#### Movie Update Route

- Route: `PATCH /api/movies/<int:movie_id>/`
- Request Body:
  ```json
  {
    "duration": "120min",
    "synopsis": "An updated synopsis."
  }
  ```
- Response (Status 200 OK):
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

### Custom Pivot Table

In this part of the project, we created an app called "movies_orders" which contains a model called "MovieOrder." This model includes the following attributes:

- `purchased_at`: A date and time automatically filled by Django when the object is inserted into the database.
- `price`: A Decimal field with a maximum of 8 digits and 2 decimal places.

