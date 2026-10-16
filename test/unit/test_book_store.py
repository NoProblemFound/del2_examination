import pytest
from src.book_store import BookStore


@pytest.mark.unit
def test_add_book():
    # Arrange - Skapar en tom Bookstore
    store = BookStore()

    # Act - Lägg till en ny bok i butiken
    book = store.addBook(
        "Guido van Rossum",
        "Ormar på ett plan"
    )

    # Assert - Kontrollera att boklistan i butiken har ökat med 1
    assert len(store.books) == 1
    assert book.author == "Guido van Rossum"


@pytest.mark.unit
def test_toggle_favorite_adds_book_to_favorites():
    # Arrange - Skapa en butik och lägg till en bok.
    store = BookStore()
    book = store.addBook(
        "Guido van Rossum",
        "Ormar på ett plan"
    )

    # Act - Markera boken som som favorit
    store.toggleFavorite(book.id)

    # Assert - Kontrollera att boken är markerad som favorit
    # och att den finns med i favoritlistan
    assert book.favorite is True
    assert book in store.favorite_books.books


@pytest.mark.unit
def test_toggle_favorite_removes_book_from_favorites():
    # Arrange - Skapa en butik och lägg till en bok.
    store = BookStore()

    book = store.addBook(
        "Guido van Rossum",
        "Ormar på ett plan"
    )

    # Act - Toggla favoritmarkeringen
    store.toggleFavorite(book.id)
    store.toggleFavorite(book.id)

    # Assert - Kontrollera att boken är inte längre är markerad som favorit
    assert book.favorite is False
    assert book not in store.favorite_books.books
