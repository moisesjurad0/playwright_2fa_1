from playwright.sync_api import Playwright, sync_playwright, expect
from otpauth import TOTP
import os


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://id.heroku.com/login")

    # ****** page 1 ******
    page.get_by_placeholder("Email address").fill(os.environ['EMAIL'])
    page.get_by_placeholder("Password").fill(os.environ['PASS'])
    page.get_by_role("button", name="Log In").click()

    # ****** page 2 ******

    # Authenticator App #9 | WORKS
    # otpauth://totp/Heroku:moises%20jurado?issuer=Heroku&secret=************SECRET_9************&algorithm=SHA1&digits=6&period=30
    totp = TOTP.from_b32encode(os.environ['SECRET_9'])
    code: int = totp.generate()
    uri = totp.to_uri("Heroku:moises jurado #9", "Heroku")
    # otpauth://totp/Heroku:moises%20jurado%20%239?secret=************SECRET_9************&issuer=Heroku&algorithm=SHA1&digits=6&period=30

    page.get_by_label("Verification Code").fill(str(code))
    page.get_by_role("button", name="Verify").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
