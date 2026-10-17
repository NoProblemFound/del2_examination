# Importerar Playwrights sync API så att vi kan styra en webbläsare
from playwright.sync_api import sync_playwright


# Körs en gång innan alla tester startar
def before_all(context):
    # Startar Playwright
    playwright = sync_playwright().start()

    # Startar en Chromium-webbläsare
    # headless=False innebär att webbläsarfönstret visas på skärmen
    browser = playwright.chromium.launch(headless=False)

    # Sparar Playwright-objektet i context
    # så att det kan användas i bdd testerna
    context.playwright = playwright

    # Sparar webbläsaren i context
    context.browser = browser

    # Öppnar en ny flik/sida i webbläsaren
    context.page = browser.new_page()


# Körs en gång efter att alla tester är klara
def after_all(context):
    # Stänger webbläsaren
    context.browser.close()

    # Stoppar Playwright och frigör resurser
    context.playwright.stop()
