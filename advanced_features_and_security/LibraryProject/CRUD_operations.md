# CRUD Operations performed in the Django Shell and their Outputs

## Create a Book

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
```

Output:

```plaintext
1984 by George Orwell (1949)
```

## Retrieve the Book

```python
retrieved_book = Book.objects.get(title="1984")
print(f"Title: {retrieved_book.title}, Author: {retrieved_book.author}, Year: {retrieved_book.publication_year}")
```

Output:

```plaintext
Title: 1984, Author: George Orwell, Year: 1949
```

## Update the Book

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
```

Output:

```plaintext
Nineteen Eighty-Four by George Orwell (1949)
```

## Delete the Book

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
```

Output:

```plaintext
<QuerySet []>
```
