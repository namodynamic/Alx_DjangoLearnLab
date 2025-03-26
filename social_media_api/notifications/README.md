# Likes and Notifications System

## Overview

This feature enhances user engagement in our Social Media API by introducing two key functionalities:

1. Post Liking System
2. Notification Mechanism

## Likes Functionality

### Notifications Endpoints

#### Like a Post Endpoint

**URL:** `api/posts/<int:pk>/like/`
**Method:** `POST`
**Authentication:** **Required**
**Description:** Allows authenticated users to like a post

#### Example Request

```http
POST api/posts/123/like/
Authorization: Bearer <your_access_token>
```

#### Successful Response

```json
{
    "detail": "Post liked successfully",
    "likes_count": 5
}
```

#### Possible Error Responses

- `400 Bad Request`: If user has already liked the post
- `401 Unauthorized`: If no valid authentication token is provided

#### Unlike a Post Endpoint

**URL:** `api/posts/<int:pk>/unlike/`
**Method:** `DELETE`
**Authentication:** `Required`
**Description:** Allows authenticated users to remove their like from a post

#### Example Request

```http
DELETE api/posts/123/unlike/
Authorization: Bearer <your_access_token>
```

#### Successful Response

```json
{
    "detail": "Post unliked successfully",
    "likes_count": 4
}
```

#### Possible Error Responses

- `400 Bad Request`: If user has not previously liked the post
- `401 Unauthorized`: If no valid authentication token is provided

### Notifications System

### Endpoints

#### View Notifications

**URL:** `api/notifications/`
**Method:** `GET`
**Authentication:** `Required`
**Description:** Retrieves all notifications for the authenticated user

 #### Example Request

```http
GET api/notifications/
Authorization: Bearer <your_access_token>
```
#### Successful Response

```json
[
    {
        "id": 1,
        "actor_username": "john_doe",
        "verb": "liked your post",
        "description": null,
        "timestamp": "2024-03-26T10:30:45.123Z",
        "is_read": false
    },
    {
        "id": 2,
        "actor_username": "jane_smith",
        "verb": "commented on your post",
        "description": null,
        "timestamp": "2024-03-25T15:20:30.456Z",
        "is_read": false
    }
]
```

#### Mark Notifications as Read

**URL:** `api/notifications/mark-read/`
**Method:** `PUT`
**Authentication:** `Required`
**Description:** Marks all unread notifications as read for the authenticated user

#### Example Request

```http
PUT api/notifications/mark-read/
Authorization: Bearer <your_access_token>
```

#### Successful Response

```json
{
    "detail": "All notifications marked as read"
}
```
