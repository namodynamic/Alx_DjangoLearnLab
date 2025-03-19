# Blog Post Management

This Django blog application allows users to create, read, update, and delete blog posts. Below are the details of each feature:

## 1. List Posts

- **URL**: `/posts/`
- **Method**: GET
- **Description**: Displays a list of all blog posts with titles and a brief snippet of content.
- **Permissions**: Accessible to all users, regardless of authentication status.

## 2. View Post Details

- **URL**: `/posts/<int:pk>/`
- **Method**: GET
- **Description**: Shows the full content of a specific blog post.
- **Permissions**: Accessible to all users.

## 3. Create Post

- **URL**: `/posts/new/`
- **Method**: GET (form) and POST (submit)
- **Description**: Allows authenticated users to create a new blog post.
- **Permissions**: Only authenticated users can create posts.
- **Data Handling**: The author of the post is automatically set to the logged-in user.

## 4. Update Post

- **URL**: `/posts/<int:pk>/edit/`
- **Method**: GET (form) and POST (submit)
- **Description**: Enables the author of a post to edit their existing blog post.
- **Permissions**: Only the author of the post can edit it.
- **Data Handling**: The author field is preserved and not editable.

## 5. Delete Post

- **URL**: `/posts/<int:pk>/delete/`
- **Method**: GET (confirmation) and POST (confirm deletion)
- **Description**: Allows the author of a post to delete their blog post.
- **Permissions**: Only the author of the post can delete it.
- **Data Handling**: The post is permanently removed from the database upon confirmation.

> - All forms include CSRF tokens `{% csrf_token %}` for security.
> - Passwords and sensitive user data are handled securely using Django's built-in mechanisms.
> - Users must be authenticated to create, update, or delete posts.

### Comment Management

- Users can read comments on blog posts.
- Authenticated users can add comments to posts.
- Users can edit or delete their own comments.

### Permissions

- Only authenticated users can post comments.
- Users can only edit or delete their own comments.

### Usage

- Comments are displayed under each blog post.
- Users can add a comment using the provided form.
- Users can edit or delete their comments from the post detail view.
