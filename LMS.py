class book:
    def __init__(self,title,author,isbn,avaliable=True):
        self._title=title
        self._author=author
        self._isbn=isbn
        self._avaliable=avaliable
    def gettitle(self):
        return self._title
    def getauthor(self):
        return self._author
    def getisbn(self):
        return self._isbn
    def getavaliable(self):
        return self._avaliable
    def setavaliable(self,avalaibale):
        self._avaliable=avalaibale
    def __str__(self):
        return ("Title: "+str(self._title)+"\n"+"Author: "+str(self._author)+"\n"+"Isbn: "+str(self._isbn)+"\n"+"Avaliable: "+str(self._avaliable))
class library:
    def __init__(self,books=[]):
        self._books=books
    def add_book(self,book):
        for book1 in self._books:
            if book1.getisbn()==book.getisbn():
                print("no can do")
                return
        self._books.append(book)
    def borrow_book(self,isbn):
        for book in self._books:
            if book.getisbn()==isbn:
                if book.getavaliable():
                    book.setavaliable(False)
                else:
                    print("no can do")
    def return_book(self,isbn):
        for book in self._books:
            if book.getisbn()==isbn:
                book.setavaliable(True)
    def list_available_books(self):
        for book in self._books:
            if book.getavaliable():
                print(book)
def main():
    # Create library
    books=[]
    library1 = library(books)

    # Add books
    book1 = book("The Pragmatic Programmer", "Andrew Hunt", "12345")
    book2 = book("Clean Code", "Robert C. Martin", "67890")
    book3 = book("Introduction to Algorithms", "Thomas H. Cormen", "54321")

    library1.add_book(book1)
    library1.add_book(book2)
    library1.add_book(book3)

    print("\n📚 Available books initially:")
    library1.list_available_books()

    # Borrow a book
    print("\n🔑 Borrowing book with ISBN 12345...")
    library1.borrow_book("12345")

    print("\n📚 Available books after borrowing:")
    library1.list_available_books()

    # Return a book
    print("\n🔙 Returning book with ISBN 12345...")
    library1.return_book("12345")

    print("\n📚 Available books after returning:")
    library1.list_available_books()

main()



