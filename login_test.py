import re
from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username", exact=True).fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(re.compile(r"/dashboard"))

