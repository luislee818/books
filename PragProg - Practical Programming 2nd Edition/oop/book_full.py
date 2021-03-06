class Book:
    """Information about a book, including title, list of authors,
    publisher, publication date, number of pages, and ISBN.
    """

    def __init__(self, title, authors, publisher, isbn):
        """ (Book, str, list of str, str, str) -> NoneType

        Create a new book entitled title, written by the people in authors,
        published by publisher, with ISBN isbn.  Make a copy of the
        authors list to avoid aliasing.
        """

        self.title = title
        # Copy the list in case the caller modifies that list later.
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn

    def num_authors(self):
        """ (Book) -> int

        Return the number of authors of this book.

        >>> pybook = Book("Practical Programming", \
            ["Campbell", "Gries", "Montojo"], \
            "Pragmatic Bookshelf", \
            "978-1-93778-545-1")
        >>> pybook.num_authors()
        3
        """

        return len(self.authors)

    def __str__(self):
        """ (Book) -> str

        Return a human-readable string representation of this Book.
        """

        return """Title: {0}
Authors: {1}
Publisher: {2}
ISBN: {3}""".format(
    self.title, ', '.join(self.authors), self.publisher, self.ISBN)

    def __eq__(self, other):
        """ (Book, Book) -> bool

        Return True iff this book and other have the same ISBN.
        """

        return self.ISBN == other.ISBN
