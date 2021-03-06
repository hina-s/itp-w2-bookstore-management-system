def create_bookstore(name):
    bookstore={
        'name' : name,
        'authors' : [],
        'books' : []
    }
    return bookstore


def get_bookstore_name(bookstore):
    
    name = bookstore['name']
    return name

def add_author(bookstore, name, nationality):
    author= {
        'name' : name,
        'nationality' : nationality
        
    }
    
    bookstore['authors'].append(author)
    return author


def get_author_by_name(bookstore, name):
    
    for author in bookstore['authors']:
        if name == author['name']:
            return author
        

def add_book(bookstore, title, isbn, author):
    book= {
        'title': title,
        'isbn' : isbn,
        'author': author
    }
        
    bookstore['books'].append(book)
    return book


def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if title == book['title']:
            return book
        

def get_books_by_author(bookstore, author):
    books = []
    for book in bookstore['books']:
        if author == book['author']:
            books.append(book)
            
    return books

            
