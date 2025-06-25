from .Book import Book

class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.All_Books = books

    def load_Library(self, csv_file_path):
        return

    def add_Book(self,title, author, publisher, publication_date, isbn):
        newBook = Book(title, author, publisher, publication_date, isbn)
        if not newBook in self.All_Books:
            self.All_Books.append(newBook)
        return

    def edit_Book(self, isbn, new_title):
        for book in self.All_Books:
            if book.isbn == isbn:
                book.title = new_title
        return

    def Display_Report(self):
        Report=""
        for book in self.All_Books:
            Report+=book.describe()
        return Report

    def Remove_Book(self, title="", isbn=""):
        if title is None and isbn is None:
            return
        for i, book in enumerate(self.All_Books):
            if (title and book.title == title) or (isbn and book.isbn == isbn):
                self.All_Books.pop(i)
                return True
        return False

    def get(self, title):
        for book in self.All_Books:
            if book.title == title:
                return book

    def Search(self, search_title="", search_author="", search_publisher="", search_isbn=""):
        list_books = []
        description ="\nWe have found for your search "
        description.join(f"\n title {search_title}")
        description.join(f"\n author {search_author}")
        description.join(f"\n publisher {search_publisher}")
        description.join(f"\n isbn {search_isbn}")

        for book in self.All_Books:
            if search_title in book.title or search_author in book.author or search_publisher in book.publisher or search_isbn== book.isbn:
                list_books.append(book)
                description.join(book.describe())
        # print(description)
        return list_books



