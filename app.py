from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://id.heroku.com/login")
    page.get_by_placeholder("Email address").click()
    page.get_by_placeholder("Email address").click()
    page.get_by_placeholder("Email address").click()
    page.get_by_placeholder("Email address").fill("moises003@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("UX3-P8vZbrad-D5")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="One-Time Password Generator Connect an authenticator app that generates verification codes.").click()
    page.locator("canvas").click()
    page.get_by_label("Verification Code").click()
    page.get_by_label("Verifier Name").click()
    page.get_by_role("button", name="Connect").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
