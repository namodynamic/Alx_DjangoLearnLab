# Retrieve and display all attributes of the book

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
```

Expected Output:

```plaintext
Title: 1984, Author: George Orwell, Publication Year: 1949
```
