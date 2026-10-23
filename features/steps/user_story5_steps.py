import re
from behave import given, when, then
from playwright.sync_api import expect

# URL till examinationssidan
exam_page = "https://tap-vt26-testautomatisering.github.io/exam/"


@given("att användaren öppnar webplatsen")
def open_website(context):
    # Öppna webbplatsen
    context.page.goto(exam_page)


@when('användaren öppnar sidan "{x}"')
def open_my_books(context, x):
    # Gå till sidan Mina böcker
    context.page.get_by_role("button", name=f"{x}").click()


@then("ska inga böcker visas i favoritlistan")
def verify_empty_favorites(context):
    # Kontrollera att ingen favoritbok visas
    expect(context.page.get_by_text(
            "När du valt, kommer dina favoritböcker att visas här."
        )).to_be_visible()


@when('användaren markerar boken "{my_favorite}" som favorit')
def mark_book_as_favorite(context, my_favorite):
    # Klicka på favoritikonen för den valda boken
    context.page.get_by_test_id(
        f"star-{my_favorite}").click()


@then('ska boken "{my_favorite}" vara favoritmarkerad')
def verify_marking(context, my_favorite):
    # Hämta favoritikonen för den valda boken
    favorite_star = context.page.get_by_test_id(f"star-{my_favorite}")
    # Kontrollera att boken har markerat som favorit
    expect(favorite_star).to_have_class("star selected")


@then('ska boken "{my_favorite}" visas i favoritlistan')
def verify_book_in_favorites(context, my_favorite):
    # Kontrollera att bokens titel visas på favoritlistan
    expect(context.page.get_by_text(my_favorite)).to_be_visible()


@when('användaren avmarkerar boken "{my_favorite}" som favorit')
def unmark_book_as_favorite(context, my_favorite):
    # Klicka på favoritikonen igen för att ta bort markeringen
    context.page.get_by_test_id(f"star-{my_favorite}").click()


@then('ska boken "{my_favorite}" inte visas i favoritlistan')
def verify_book_not_in_favorites(context, my_favorite):
    # Kontrollera att boken inte längre finns i favoritlistan
    expect(context.page.get_by_text(my_favorite)).not_to_be_visible()

