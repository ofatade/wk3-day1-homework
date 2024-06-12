# Task 1: Library System Enhancement

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book_to_library(library, new_book):
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} is already in the library.")
    else:
        library.append(new_book)
        print(f"The book '{new_book[0]}' by {new_book[1]} has been added to the library.")
        print(library)


new_books = ("The Gods are dead", "Chinua Achebe")#("1984", "George Orwell")#('Fahrenheit 451', 'Ray Bradbury')("The Gods are dead", "Chinua Achebe")




add_book_to_library(library, new_books)