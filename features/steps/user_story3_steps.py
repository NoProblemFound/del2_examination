from behave import given, when, then
from playwright.sync_api import Page, expect

exam_page = "https://tap-vt26-testautomatisering.github.io/exam/"


@given("att användaren öppnar sidan Lägg till bok")
def open_add_book_page(context):
    # Öppna webbsidans startsida
    context.page.goto(exam_page)
    # Klicka på knappen "Lägg till bok"
    # för att gå till formuläret där en ny bok kan läggas till.
    context.page.get_by_role("button", name="Lägg till bok").click()


@then("ska ett fält för titel visas")
def verify_title_field(context):
    # Verifiera att fältet med etiketten "Titel"
    # visas på sidan för användaren
    expect(context.page.get_by_label("Titel")).to_be_visible()


@then("ska ett fält för författare visas")
def verify_author_field(context):
    # Kontrollera att fältet med etiketten "Författare"
    # är synligt för användaren.
    expect(context.page.get_by_label("Författare")).to_be_visible()


@then('knappen "Lägg till ny bok" vara inaktiverad')
def verify_disabled_button(context):
    # Kontrollera att knappen "Lägg till ny bok"
    # är inaktiverad
    expect(context.page.get_by_role("button", name="Lägg till ny bok"
        ) ).to_be_disabled()


@when("användaren fyller i titel och författare")
def fill_book_information(context):
    # Fyll i fältet "Titel"
    context.page.get_by_label("Titel").fill("Min bok")
    # Fyll i fältet "Författare" ett någonting.
    context.page.get_by_label("Författare").fill("Min författare")


@then('ska knappen "Lägg till ny bok" vara aktiverad')
def verify_enabled_button(context):
    # Kontrollera att knappen "Lägg till ny bok"
    # är aktiverad och kan användas av användaren
    expect(context.page.get_by_role("button", name="Lägg till ny bok"
        )).to_be_enabled()
