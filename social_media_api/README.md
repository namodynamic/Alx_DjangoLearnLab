# Social Media API

This is a Django-based RESTful API for a social media platform. The API allows users to register, authenticate, and interact with the platform. Below, you'll find instructions for setting up the project, registering and authenticating users, and a detailed overview of the endpoints.

---

## Features

- User Registration
- User Authentication with Token-based Auth
- Profile Management
- Follow/Unfollow Users
- Custom User Model with Extended Fields

## Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

## Setup Process

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd social_media_api
   ```

2. **Create and Activate Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**:

   - Edit the `settings.py` file to configure your database settings.
   - Run `python manage.py makemigrations accounts` to create database migrations and `python manage.py migrate` to apply them.

5. **Create Superuser (optional)**:

   - Run `python manage.py createsuperuser` to create a superuser account.

6. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the API**: Open your browser or API client (e.g., Postman) and navigate to `http://127.0.0.1:8000/api/` to interact with the API endpoints.

Live Url: [https://namodynamic.pythonanywhere.com/](https://namodynamic.pythonanywhere.com/)


### User Registration and Authentication

#### Register a New User

To register a new user, send a POST request to `/api/register/` with the following data:

```json
{
    "username": "your_username",
    "email": "your_email@example.com",
    "password": "your_password"
}
```

####  Obtain User Token

To obtain a user token, send a POST request to `/api/token/` with the following data:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

The response will include an access token and a refresh token.

```json
{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}
```

#### Refresh User Token

To refresh a user token, send a POST request to `/api/token/refresh/` with the following data:

```json
{
    "refresh": "your_refresh_token"
}
```

## User Model Overview

The user model includes the following fields:

- `id`: Unique identifier for the user.
- `username`: Username of the user.
- `email`: Email address of the user.
- `password`: The hashed password of the user.
- `date_joined`: Date when the user joined the platform.

## API Endpoints

1. **User Registration**

   - Endpoint: `/api/register/`
   - Method: `POST`
   - Description: Register a new user.
   - Request Payload:

     ```json
     {
         "username": "your_username",
         "email": "your_email@example.com",
         "password": "your_password"
     }
     ```

   - Response:

     ```json   
     {
         "id": 1,
         "username": "your_username",
         "email": "your_email@example.com",
         "date_joined": "2023-09-27T12:34:56.789Z"
     }
     ```

2. **User Authentication**

   - Endpoint: `/api/token/`
   - Method: `POST`
   - Description: Authenticate a user and return an access and refresh token.
   - Request Payload:

     ```json
     {
         "username": "your_username",
         "password": "your_password"
     }
     ```

   - Response:

     ```json
     {
         "access": "your_access_token",
         "refresh": "your_refresh_token"
     }
     ```

3. **Refresh User Token**

   - Endpoint: `/api/token/refresh/`
   - Method: `POST`
   - Description: Refresh an existing user token.
   - Request Payload:

     ```json
     {
         "refresh": "your_refresh_token"
     }
     ```

   - Response:

     ```json
     {
         "access": "your_access_token"
     }
     ```

4. **User Profile**

   - Endpoint: `/api/profile/`
   - Method: `GET`
   - Description: Retrieve the profile details of the authenticated user.
   - Response:

     ```json
     {
         "id": 1,
         "username": "your_username",
         "email": "your_email@example.com",
         "date_joined": "2023-09-27T12:34:56.789Z"
     }
     ```

     ## Usage Example
     
     Example: Registering a User

     ```bash
     curl -X POST http://127.0.0.1:8000/api/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "exampleuser", "email": "I1s6Z@example.com", "password": "password123"}'
     ``` 
     
     Example: Accessing User Profile

     ```bash
     curl -X GET http://127.0.0.1:8000/api/profile/ \
     -H "Authorization: Bearer <access_token>"
     ```
