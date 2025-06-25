class Book:
    def __init__(self, title, author, publisher, publication_date, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.isbn = isbn

    def repr(self):
        return f"{self.title} by {self.author}"


class BookStoreInventory:
    def __init__(self):
        self.books = []

    def __inti__(self, list_of_Books):
        self.books = list_of_Books

    def add_book(self, book):
        self.books.append(book)

    def edit_book(self, isbn, new_title):
        for book in self.books:
            if book.isbn == isbn:
                book.title = new_title
                break

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                break

    def search_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def search_by_author(self, author):
        for book in self.books:
            if book.author == author:
                return book
        return None

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_inventory(self):
        print(f"Total number of books: {len(self.books)}")

        authors = {}
        for book in self.books:
            if book.author in authors:
                authors[book.author] += 1
            else:
                authors[book.author] = 1
        print("Number of books by each author:")
        for author, count in authors.items():
            print(f"{author}: {count}")

        publishers = {}
        for book in self.books:
            if book.publisher in publishers:
                publishers[book.publisher] += 1
            else:
                publishers[book.publisher] = 1
        print("Number of books published by each publisher:")
        for publisher, count in publishers.items():
            print(f"{publisher}: {count}")

    def read_inventory(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                title, author, publisher, publication_date, isbn = line.strip().split(",")
                new_book = Book(title = title, author= author, publisher= publisher, publication_date= publication_date, isbn= isbn)
                self.books.append(new_book)

    def write_inventory(self, filename):
        with open(filename, "w") as f:
            for book in self.books:
                f.write(f"{book.title},{book.author},{book.publisher},{book.publication_date},{book.isbn}\n")

    def append_book(self, book, filename):
        with open(filename, "a") as f:
            f.write(f"{book.title},{book.author},{book.publisher},{book.publication_date},{book.isbn}\n")

    def remove_book(self, isbn, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        with open(filename, "w") as f:
            for line in lines:
                fields = line.strip().split(",")
                if len(fields) == 5:
                    line_isbn = fields[4]
                    if line_isbn == isbn:
                        continue
                f.write(line)

    def display_inventory(self):
        print(f"Total number of books: {len(self.books)}")
        authors = {}
        for book in self.books:
            if book.author in authors:
                authors[book.author] += 1
            else:
                authors[book.author] = 1
                print("Number of books by each author:")
        for author, count in authors.items():
            print(f"{author}: {count}")


OurLibrary = BookStoreInventory()
OurLibrary.read_inventory("data.csv")
OurLibrary.display_inventory()
