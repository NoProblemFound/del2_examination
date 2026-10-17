import pytest
from src.book_store import BookStore


@pytest.fixture
def f_store():
    return BookStore()


def test_toggle_favorite_updates_favorite_books(f_store):
    # Arrange - Bookstore-objektet skapas genom fixture
    # Lägg till en bok i Bookstore
    book = f_store.addBook(
        "Guido van Rossum",
        "Ormar på ett plan"
    )
    # Act - Markera boken som favorit
    f_store.toggleFavorite(book.id)

    # Assert - Kontrollera favoritlistan innehåller en bok
    # och att den markerade boken finns med i listan.
    assert len(f_store.favorite_books.books) == 1
    assert f_store.favorite_books.books[0] == book


def test_toggle_favorite_twice_removes_book(f_store):
    # Arrange -
    book = f_store.addBook(
        "Guido van Rossum",
        "Ormar på ett plan"
    )

    # Act - Markera och avmarkera en bok som favorit
    f_store.toggleFavorite(book.id)
    f_store.toggleFavorite(book.id)

    # Assert - Det skall inte finnas någon bok i favoritlistan
    assert len(f_store.favorite_books.books) == 0
