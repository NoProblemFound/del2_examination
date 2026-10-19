from behave import given, when, then
from playwright.sync_api import Page, expect

exam_page = "https://tap-vt26-testautomatisering.github.io/exam/"



@given("att användaren öppnar webbsidan")
def open_website(context):
    # Gå til startsida
    context.page.goto(exam_page)


@when('användaren klickar på knappen "Lägg till bok"')
def click_add_book(context):
    # Klicka på "Lägg till bok"
    context.page.get_by_role("button", name="Lägg till bok").click()


@when('användaren fyller i titelfältet med "Min bok"')
def input_title(context):
    # Skriv en titel
    context.page.get_by_label("Titel").fill("Min bok")


@when('användaren fyller i författarfältet med "Min författare"')
def input_author(context):
    # Fyller i en författare
    context.page.get_by_label("Författare").fill("Min författare")


@when('användaren klickar på knappen "Lägg till ny bok"')
def store_a_new_book(context):
    # Klicka på "Lägg till ny bok
    context.page.get_by_role("button", name="Lägg till ny bok").click()


@then("ska titel- och författarfälten vara tomma")
def verify_empty_fields(context):
    # Kontrollera att titel- och författarfälten är tomma
    expect(context.page.get_by_label("Titel")).to_have_value("")
    expect(context.page.get_by_label("Författare")).to_have_value("")


@when("användaren öppnar katalogen")
def open_catalog(context):
    # Klickar på Katalog
    context.page.get_by_role("button", name="Katalog").click()


@then("ska den nya boken visas längst ner i listan")
def verify_new_book_last(context):
    books = context.page.locator("div.book")

    # Hämtar sista boken i listan
    last_book = books.last

    expect(last_book).to_contain_text("Min bok")
    expect(last_book).to_contain_text("Min författare")