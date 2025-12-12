def search_book_by_name(name, collection):
    """Searches for a book by name in the collection and returns it as a dictionary"""
    # TODO: implement this function

def add_book(new_book, collection):
    """Check if the ISBN of the book is unique and then add it to the colllection."""
    # TODO: implement this function

def remove_book(isbn, collection):
    """Remove a book from the collection based on the isbn"""
    # TODO: implement this function

def borrow_book(book):
    """Decrese the number of available books by one. If already zero it raises an error."""
    # TODO: implement this function

def return_book(book):
    """Increase the bumber of available books by one. If the total number is exceeded this should be increased too."""
    # TODO: implement this function

def filter_for_available_books(collection):
    """Returns a new list with only books which are available."""
    # TODO: implement this function

def filter_for_borrowed_books(collection):
    """Returns a new list with all books where at least one is not available."""
    # TODO: implement this function