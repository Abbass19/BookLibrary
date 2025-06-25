class Book:
    def __init__(self, title, author, publisher, publication_date, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.isbn = isbn

    def edit(self, new_title=None, new_author=None, new_publisher=None, new_publication_date=None, new_isbn=None):
        if new_title is not None:
            self.title = new_title
        if new_author is not None:
            self.author = new_author
        if new_publisher is not None:
            self.publisher  = new_publisher
        if new_publication_date is not None:
            self.publication_date = new_publication_date
        if new_isbn is not None:
            self.isbn = new_isbn

    def get_title(self):
        return self.title

    def describe(self):
        return f"\nThe Book {self.title} is written by {self.author} published by {self.publisher} at {self.publication_date}"