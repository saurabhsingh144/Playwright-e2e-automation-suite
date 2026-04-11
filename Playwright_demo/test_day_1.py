from playwright.sync_api import Page, expect
from playwright.async_api import async_playwright

def test_day_code_1(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    expect(page).to_have_title("Automation Testing Practice")

def test_day_code_2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")



