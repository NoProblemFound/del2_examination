import pytest
from src.book_store import BookStore


@pytest.fixture
def f_store():
    return BookStore()


@pytest.fixture
def f_book(f_store):
    return f_store.addBook(
        "Guido van Rossum",
        "Ormar på ett plan"
    )


@pytest.mark.unit
def test_add_book(f_store):
    # Arrange - Genom fixture

    # Act - Lägg till en ny bok i butiken
    book = f_store.addBook(
        "Guido van Rossum",
        "Ormar på ett plan"
    )

    # Assert - Kontrollera att boklistan i butiken har ökat med 1
    assert len(f_store.books) == 1
    assert book.author == "Guido van Rossum"


@pytest.mark.unit
def test_toggle_favorite_adds_book_to_favorites(f_store, f_book):
    # Arrange - Genom fixturer

    # Act - Markera boken som som favorit
    f_store.toggleFavorite(f_book.id)

    # Assert - Kontrollera att boken är markerad som favorit
    # och att den finns med i favoritlistan
    assert f_book.favorite is True
    assert f_book in f_store.favorite_books.books


@pytest.mark.unit
def test_toggle_favorite_removes_book_from_favorites(f_store, f_book):
    # Arrange - Genom fixturer.

    # Act - Toggla favoritmarkeringen
    f_store.toggleFavorite(f_book.id)
    f_store.toggleFavorite(f_book.id)

    # Assert - Kontrollera att boken är inte längre är markerad som favorit
    assert f_book.favorite is False
    assert f_book not in f_store.favorite_books.books
