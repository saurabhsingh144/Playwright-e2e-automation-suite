import re

from playwright.sync_api import Page, expect


def test_orange_hrm(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role(role="button",name="Login").click()
    page.wait_for_timeout(5000)
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()


