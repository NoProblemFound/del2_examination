from behave import given, when, then
from playwright.sync_api import Page, expect


exam_page = "https://tap-vt26-testautomatisering.github.io/exam/"


@given(u'att användaren öppnar startsidan')
def open_webpage(context):
    #Gå till startsidan
    context.page.goto(exam_page)


@then('ska titeln "Läslistan" visas högst upp på sidan')
def verify_title(context):
    # Kontrollera att sidans huvudtitel visas
    expect(context.page.get_by_role("heading", name="Läslistan")).to_be_visible()


@then('rubriken "Välkommen!" visas')
def verify_welcome_heading(context):
    # Kontrollera att välkomstrubriken visas
    expect(context.page.get_by_role("heading", name="Välkommen!")).to_be_visible()


@then('texten "Sidan för dig som gillar att läsa. Välj dina favoriter." visas')
def verify_welcome_text(context):
    # Kontrollera att välkomsttexten visas
    expect(context.page.get_by_text(
        "Sidan för dig som gillar att läsa. Välj dina favoriter."
    )).to_be_visible()
