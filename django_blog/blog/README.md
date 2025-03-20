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

## Tagging and Search Features

This documentation outlines how to use the tagging and search features within the blog application. These features enhance the organization and discoverability of content, allowing users to categorize posts via tags and search for posts based on keywords.

### Tagging Posts

Tags allow users to categorize blog posts, making it easier to find related content. Here's how to add tags to your posts:

1. **Creating a Post with Tags**:
   When creating a new blog post, you can add tags in the post creation form. Simply enter the desired tags in the tags field. If the tag does not already exist, it will be created automatically.

   Example:
   - Title: "Understanding Django"
   - Content: "This post covers the basics of Django."
   - Tags: `Django`, `Web Development`, `Python`

2. **Editing a Post to Add or Change Tags**:
   To modify the tags of an existing post, navigate to the edit page of the post. You can add new tags or remove existing ones in the tags field.

3. **Viewing Tags**:
   Tags associated with a post will be displayed on the post detail page. Each tag is clickable and will link to a filtered view showing all posts containing that tag.

### Searching for Posts

The search feature allows users to find posts based on keywords in the title, content, or tags. Here's how to utilize the search functionality:

1. **Using the Search Bar**:
   At the top of the blog, you will find a search bar. Enter keywords related to the content you are looking for. This can include:
   - Words from the post title
   - Keywords from the post content
   - Tags associated with the posts

2. **Executing a Search**:
   After entering your search query, press Enter or click the search button. The application will display a list of posts that match your search criteria.

3. **Viewing Search Results**:
   The search results page will show all posts that contain the keywords in their title, content, or tags. You can click on any post title to view the full content.

### Example Usage

- **Adding Tags**: When creating or editing a post, simply type the tags in the designated field. For example, typing "Django" and "Python" will associate those tags with the post.
  
- **Searching for Content**: If you want to find posts related to "Django", type "Django" in the search bar and hit Enter. The results will display all posts that mention "Django" in their title, content, or tags.
