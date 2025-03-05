# API Authentication & Permissions Guide

## Overview

This document explains how authentication and permissions are set up in this Django REST Framework (DRF) API to secure endpoints and restrict access to authorized users only.

---

## Step 1: Authentication Setup

Our API uses **Token Authentication**, which means users must send a token with each request to access protected endpoints.

### 1️⃣ Enable Token Authentication in `settings.py`

Add `rest_framework.authtoken` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'api',
]
```

Then apply migrations:

```bash
python manage.py migrate
```

### 2️⃣ Configure Authentication in `settings.py`

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",  # Token-based authentication
        "rest_framework.authentication.SessionAuthentication",  # Optional for Django Admin login
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",  # Restrict access to authenticated users
    ],
}
```

### 3️⃣ Create a User and Generate Authentication Token

To use the API, we need to create a user and generate a token for them

#### Create a User in Django Shell

```bash
python manage.py shell

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create a new user
user = User.objects.create_user(username="john_doe", password="password123")

# Generate a token for the user
token, created = Token.objects.get_or_create(user=user)
print(f"Token for {user.username}: {token.key}")
```

Now, `john_doe` have a unique tokens for authentication

### 4️⃣ API Endpoint for Token Authentication

Provide a built-in endpoint for users to retrieve their token:

#### Define the token endpoint in `api/urls.py`

```python
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("api/token/", obtain_auth_token, name="api_token_auth"),
]
```

#### Request a Token Using Postman or curl

```bash
curl -X POST http://127.0.0.1:8000/api/token/ -d "username=john_doe&password=password123"
```

✅ **Response:**

```json
{
  "token": "your_generated_token_here"
}
```

**Now, the user can authenticate using this token!**

---

## 🔑 Step 2: Permissions Setup

Permissions **control which users can access API endpoints**.

### 1️⃣ Apply Built-in Permissions to Views

Edit `views.py` to restrict access based on authentication status:

```python
from rest_framework import generics, permissions
from .serializers import BookSerializer
from .models import Book

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access
```

 **Now, unauthenticated users cannot access this API.**

---

## Step 3: Testing Authentication & Permissions

```bash
curl -H "Authorization: Token your_generated_token_here" http://127.0.0.1:8000/api/books/
```

✅ **Response:**

```json
[
    {
        "id": 1,
        "title": "Django for Beginners",
        "author": "William S. Vincent"
    },
    {
        "id": 2,
        "title": "Python Crash Course",
        "author": "Eric Matthes"
    }
]
```

---

## 📌 Summary

✅ **Enabled Token Authentication in `settings.py`**  
✅ **Created a token retrieval endpoint (`/api/token/`)**  
✅ **Applied permissions to restrict API access**  
✅ **Tested authentication & permissions with Postman and curl**
