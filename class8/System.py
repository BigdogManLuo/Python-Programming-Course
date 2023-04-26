class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def show_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from the library.")
        else:
            print("This book is not in the library.")

    def show_all_books(self):
        print("Library contains the following books:")
        for book in self.books:
            book.show_info()
            print("\n")
            
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("1984", "George Orwell", 1949)

my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.show_all_books()

my_library.remove_book(book2)

my_library.show_all_books()
def main_menu():
    print("\nWelcome to the Library Management System!")
    print("Please select an option:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Show all books")
    print("4. Exit")
    return input("Enter the number of your choice: ")

def get_book_info():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    publication_year = int(input("Enter book publication year: "))
    return title, author, publication_year

my_library = Library()

while True:
    choice = main_menu()
    
    if choice == '1':
        title, author, publication_year = get_book_info()
        new_book = Book(title, author, publication_year)
        my_library.add_book(new_book)
        
    elif choice == '2':
        title, author, publication_year = get_book_info()
        book_to_remove = None
        
        for book in my_library.books:
            if book.title == title and book.author == author and book.publication_year == publication_year:
                book_to_remove = book
                break
                
        if book_to_remove is not None:
            my_library.remove_book(book_to_remove)
        else:
            print("This book is not in the library.")
            
    elif choice == '3':
        my_library.show_all_books()
        
    elif choice == '4':
        print("Goodbye!")
        break
        
    else:
        print("Invalid option. Please try again.")
