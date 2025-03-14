# Advanced API Project

## Views Configuration

### ListView

- URL: `/api/books/`
- Method: GET
- Description: Lists all books in the system with filtering, searching, and ordering capabilities.
- Filtering: Use query parameters to filter by `title`, `author`, and `publication_year`.
  - Example: `/api/books/?title=Book Title`
- Searching: Use the `search` query parameter to search by `title` or `author`.
  - Example: `/api/books/?search=Author Name`
- Ordering: Use the `ordering` query parameter to order by `title` or `publication_year`.
  - Example: `/api/books/?ordering=publication_year`

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

## Testing Strategy

Used Django's APITestCase from rest_framework.test to ensure that API endpoints work as expected. The tests are structured as follows:

1. **Setup (`setUp` method)** – Creates a test user, author, and book before each test runs.
2. **Test cases** – Individual methods that test specific API functionalities. The test cases validate the functionality of book-related endpoints, including filtering, searching, ordering, creating, updating, and deleting books.
3. **Assertions**– Validates that the expected behavior matches the actual response.

Each test case follows the structure:

- Define the API endpoint using reverse().

- Make an HTTP request (`GET`, `POST`, `PUT`, `DELETE`).

- Validate the response status code.

- Check the response data (if applicable).

### Running the Tests

To run the test suite, execute the following command:

```bash
python manage.py test api
```

Expected Output:

```plaintext
Found X test(s)
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran X tests in Y seconds

OK
Destroying test database for alias 'default'...
```

If a test fails, Django will provide details on the failed test and the assertion error.

### Individual Test Cases

1. `test_filter_books` – Tests Filtering by author, title, and publication_year

- **Description**: Ensures that books can be filtered based on attributes (e.g., publication year).
- **HTTP Request**: `GET /api/books/`
- **Expected Behavior**: The API returns books matching the filter criteria.
- **Assertions**:
  - Response status code is `200 OK`.
  - The number of books in the response matches the expected count.

2. `test_search_books` – Tests Searching by title or author

- **Description**: Ensures books can be searched using the title field.
- **HTTP Request**: `GET /api/books/`
- **Expected Behavior**: Only books with a matching title are returned.
- **Assertions:**
  - Response status code is `200 OK`.
  - The returned books match the search query.

3. `test_order_books` – Tests Sorting by title or author

- **Description**: Verifies that books can be ordered by specified fields (e.g., title, publication year).
- **HTTP Request**: `GET /api/books/`
- **Expected Behavior**: Books are returned in the specified order.
- **Assertions**:
  - Response status code is `200 OK`.
  - The response list is sorted correctly.

4. `test_create_book` – Tests Creating a New Book

- **Description**: Ensures that a book can be successfully created.
- **HTTP Request**: `POST /api/books/`
- **Expected Behavior**: A new book entry is created in the database.
- **Assertions:**
  - Response status code is `201 Created`.
  - The number of books in the database increases by one.

5. `test_update_book` – Tests Updating an Existing Book

- **Description:** Validates that book details can be updated.
- **HTTP Request**: PUT /api/books/{id}/
- **Expected Behavior**: The book’s details are modified in the database.
- **Assertions**:
  - Response status code is 200 OK.
  - The book’s title is updated as expected.  

6. test_delete_book – Tests Deleting a Book

- **Description**: Verifies that a book can be deleted.
- **HTTP Request**: DELETE /api/books/{id}/
- **Expected Behavior**: The book is removed from the database.
- **Assertions**:
  - Response status code is 204 No Content.
  - The book count decreases by one.

7. test_list_books – Tests Listing All Books

- **Description**: Checks that all available books are listed.
- **HTTP Request**: GET /api/books/
- **Expected Behavior**: Returns a list of all books.
- **Assertions**:
  - Response status code is 200 OK.

### Debugging Test Failures

If a test fails, check the error message in the terminal. Common issues include:

- Incorrect URL names (reverse('api:book-list') should match urls.py).

- Missing authentication (ensure the test user is logged in).
