from behave import given, when, then
from playwright.sync_api import expect

exam_page = "https://tap-vt26-testautomatisering.github.io/exam/"


@given("att användaren öppnar webplatsen")
def open_website(context):
    # Öppna webbplatsen
    context.page.goto(exam_page)


@when('användaren öppnar sidan "Mina böcker"')
def open_my_books(context):
    # Gå till sidan Mina böcker
    context.page.get_by_role("button", name="Mina böcker").click()