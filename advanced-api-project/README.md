# Advanced API Project

## Views Configuration

### ListView

- URL: `/api/books/`
- Method: GET
- Description: Lists all books in the system.

### DetailView

- URL: `/api/books/<int:pk>/`
- Method: GET
- Description: Retrieves a single book by ID.

### CreateView

- URL: `/api/books/create/`
- Method: POST
- Description: Creates a new book. Only authenticated users can access this view.

### UpdateView

- URL: `/api/books/update/<int:pk>/`
- Method: PUT
- Description: Updates an existing book. Only authenticated users can access this view.

### DeleteView

- URL: `/api/books/delete/<int:pk>/`
- Method: DELETE
- Description: Deletes a book. Only authenticated users can access this view.

## Permissions

- `CreateView`, `UpdateView`, and `DeleteView` are protected with `IsAuthenticated` permission class to ensure only authenticated users can create, update, or delete books.
- `ListView` and `DetailView` are accessible to all users.
