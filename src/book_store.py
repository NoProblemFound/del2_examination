from src.book import Book
from src.fav_books import FavoriteBooks


class BookStore:
    def __init__(self):
        # Skapar en tom lista där alla böcker sparas
        self.books = []

        # Skapar ett objekt av FavoriteBooks som håller reda på favoritböcker
        self.favorite_books = FavoriteBooks()
        # Ett startvärde, ett godtyckligt värde över 115.
        self.next_id = 200

    def addBook(self, author, title):
        # Skapar ett nytt book objekt
        book = Book(self.next_id, author, title)
        # Lägger till boken i listan
        self.books.append(book)
        # Ökar id med 1 så nästa bok får ett unikt nummer.
        self.next_id += 1
        return book

    # Markera/Avmarkera favoritbok
    def toggleFavorite(self, book_id):
        # Loopar genom booklistan
        for book in self.books:
            if book.id == book_id:
                # Avmarkera boken om den är markerad som en favorit.
                if book.favorite:
                    book.favorite = False
                    # Tar bort boken från Favoritlistan
                    self.favorite_books.remove(book)
                else:
                    # Annars markera boken favorit
                    book.favorite = True
                    self.favorite_books.add(book)
                return book

        # Utifall om boken inte finns med i listan.
        raise ValueError("Book not found")
