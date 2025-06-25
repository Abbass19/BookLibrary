import sys

from .Library import Library
from .Book import Book
import csv

csv_path = r"C:\Users\Abbass Zahreddine\Documents\GitHub\BookLibrary\Code\Library_Code\Files\data.csv"


def load_books_from_csv(file_path):
    fetched_books = []
    fieldnames = ['Book Title', 'Author', 'Publisher', 'Publication Date', 'ISBN']  # your expected columns

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            book = Book(
                title=row['Book Title'],
                author=row['Author'],
                publisher=row['Publisher'],
                publication_date=row['Publication Date'],
                isbn=row['ISBN']
            )
            fetched_books.append(book)
    return fetched_books


def save_books_to_csv(Library, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Book title', 'author', 'publisher', 'publication date', 'isbn']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for book in Library.All_Books:
            writer.writerow({
                'Book title': book.title,
                'author': book.author,
                'publisher': book.publisher,
                'publication date': book.publication_date,
                'isbn': book.isbn
            })



#Here we Define the Input Output System Dialogue:

def print_intro_instructions():
    Instructions = ""
    Instructions += "\nWelcome to Our Library_Code"
    Instructions += "\n     To Display the books we have, type: Display"
    Instructions += "\n     To Add a new Book, type: Add"
    Instructions += "\n     To remove a Book, type Remove"
    Instructions += "\n     To exit the Software type exit"
    print(Instructions)

def Add_procedure(Our_Library):
    try:
        input_title      = input("Type the Title of the Book: ")
        input_author     = input("Type the Author of the Book: ")
        input_publisher  = input("Type the Publisher of the Book: ")
        input_date       = input("Type the Publication Date: ")
        input_isbn       = input("Type the ISBN for the Book: ")

        Our_Library.add_Book(
            title=input_title,
            author=input_author,
            publisher=input_publisher,
            publication_date=input_date,
            isbn=input_isbn
        )
        print("✅ Book added successfully!")

    except Exception as e:
        print("❌ Something went wrong while adding the book.")
        print(f"Error: {e}")


def Edit_procedure(Our_Library):
    try:
        title_search = input("Search through the database with the title : ")
        searched_Books = Our_Library.Search(search_title = title_search, search_author=title_search, search_isbn=title_search)
        for i, book in enumerate(searched_Books):
            print(f"{i}, {book.describe()}")
        Books_choice = input("Confirm what book you need to edit through entering the number: ")
        Book_To_Edit = searched_Books[Books_choice]

        print(f"    We will pass through parameters of the Book {Book_To_Edit.get_title()}")
        print(f"    If you don't Want to edit the parameter Press Enter")
        edited_title = input("   Type the Title of the Book: ")
        edited_author = input("  Type the Author of the Book: ")
        edited_publisher = input("   Type the Publisher of the Book: ")
        edited_isbn = input("    Type the ISBN for the Book: ")
        Our_Library.get(Book_To_Edit.get_title).edit(new_title=edited_title, new_author=edited_author, new_publisher=edited_publisher, new_isbn=edited_isbn)
        print("The Book had been Edited")

    except Exception as e:
        print("Something went wrong while Searching for the Book")
        print(f"Error : {e}")
    return


def Search_procedure(Our_Library):
    try:
        title_search = input("Search through the database with the title : ")
        searched_Books = Our_Library.Search(search_title = title_search, search_author=title_search, search_isbn=title_search)
        for i, book in enumerate(searched_Books):
            print(f"{i}, {book.describe()}")
    except Exception as e:
        print("Something went wrong while Searching for the Book")
        print(f"Error : {e}")
    return


def Remove_procedure(Our_Library):
    try:
        title_search = input("Input the Title of the Book to Remove: ")
        searched_Books = Our_Library.Search(search_title = title_search, search_author=title_search, search_isbn=title_search)
        Book_To_Remove = searched_Books[0]
        if Our_Library.Remove_Book(Book_To_Remove):
            print("The Book has been removed")
        else:
            print("The Book was not found to be removed")
    except Exception as e:
        print("Something went wrong while Searching for the Book")
        print(f"Error : {e}")
    return



def Exit_Procedure(Our_Library,csv_path):
    save_books_to_csv(Our_Library, csv_path)
    sys.exit()



def Interact(Our_Library, csv_path):
    while True:
        print_intro_instructions()
        print("-----------------------------------------------------------------------")
        instruction = input("Waiting for Your Instructions")
        instruction = instruction.replace(" ", "").lower()
        print(f"    Your instruction was {instruction}")
        if instruction == "display":
            print("     Activating Display" )
            print(Our_Library.Display_Report())
            continue
        elif instruction == "add":
            print("     Activating Add : ")
            Add_procedure(Our_Library)
            continue
        elif instruction == "edit":
            print("     Activating Edit : ")
            Edit_procedure(Our_Library)
            continue
        elif instruction == "remove":
            print("     Activating Remove: ")
            Remove_procedure(Our_Library)
            continue
        elif instruction == "search":
            print("     Activating Search : ")
            Search_procedure(Our_Library)
            continue
        if instruction ==  "exit":
            Exit_Procedure(Our_Library, csv_path)
            continue




def Start():
    csv_path = r"C:\Users\Abbass Zahreddine\Documents\GitHub\BookLibrary\Code\Library_Code\Files\data.csv"
    fetched_books = load_books_from_csv(csv_path)
    App_Library = Library(books=fetched_books)
    Interact(App_Library, csv_path)
