# Command to Create a Book instance

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984",author="George Orwell",publication_year=1949)

book.save()

print(book)
```

Expected Output:

```plaintext
1984 by George Orwell (1949)
```
