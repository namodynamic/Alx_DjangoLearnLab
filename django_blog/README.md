# Django Blog Authentication System

## Overview

This project includes a comprehensive user authentication system for a Django blog. It supports user registration, login, logout, and profile management.

## Features

- User registration with email
- User login and logout
- Profile management (view and update profile)

## Setup

1. **Create project folder**:

    ```bash
    mkdir django_blog
    cd django_blog
    ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Django**:

   ```bash
   pip install django
   ```

4. **Create a Django project**:

   ```bash
   django-admin startproject django_blog ./
   ```

5. **Create a new Django app called blog**:

   ```bash
    python manage.py startapp blog
   ```

6. **Register the  new blog app**: Add `'blog'` to 'INSTALLED_APPS' in 'django_blog/settings.py'

7. **Run migrations**:

   ```bash
   python manage.py makemigrations blog
   python manage.py migrate
   ```

8. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

9. **Open your browser and navigate to** `http://localhost:8000/`

- Register a new user at `http://localhost:8000/register/`
- Login with your credentials at `http://localhost:8000/login/`
- View and update your profile at `http://localhost:8000/profile/`

## Security

- All forms use CSRF tokens to protect against cross-site request forgery attacks.
- Passwords are securely hashed using Django's built-in password hashing algorithm.
