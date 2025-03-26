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
