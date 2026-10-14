import pytest

from src.book import Book
from src.fav_books import FavoriteBooks

@pytest.fixture
def my_favorites():
    return FavoriteBooks()

@pytest.fixture
def my_book():
    return Book(
        100,
        "Guido van Rossum",
        "Ormar på ett plan"
    )

@pytest.mark.unit
def test_add_book_to_favorites(my_favorites, my_book):
    # Arrange - Genom fixures ovan

    # Act - Anropa metoden som ska testas
    my_favorites.add(my_book)

    # Assert - Kontrollera att favoritlistan innehåller en bok
    # och att den tillagda boken finns i listan
    assert len(my_favorites.books) == 1
    assert my_book in my_favorites.books

@pytest.mark.unit
def test_remove_book_from_favorites(my_favorites, my_book   ):

    #Arrange - Genom fixtuers
    my_favorites.add(my_book)

    #Act - Testar metoderna

    my_favorites.remove(my_book)

    assert len(my_favorites.books) == 0
    assert my_book not in my_favorites.books
