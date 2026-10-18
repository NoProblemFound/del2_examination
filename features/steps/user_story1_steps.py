from behave import given, when, then
from playwright.sync_api import Page, expect


exam_page = "https://tap-vt26-testautomatisering.github.io/exam/"


@given(u'att användaren öppnar webbplatsen')
def open_webpage(context):
    context.page.goto(exam_page)


@then('visas knappen "{button_name}"')
def verify_button(context, button_name):
    expect(context.page.get_by_role("button", name=button_name)
    ).to_be_visible()


@then('en lista med böcker visas')
def verify_book_list(context):
    # Letar efter element som matchar div.book
    books = context.page.locator("div.book")
    # Antalet bör vara större än 0, egentligen 13.
    assert books.count() > 0
