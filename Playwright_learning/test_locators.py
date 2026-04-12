# from playwright.async_api import expec
from playwright.sync_api import Page,expect

def test_locators(page:Page):
    page.goto("https://automationexercise.com")
    '''GET BY ALT TEXT'''
    # page.wait_for_timeout()
    logo=page.get_by_alt_text("Website for automation practice")
    expect(logo).to_be_visible()
    '''CLOSE THE BROWSER INSTANCE'''
    page.close()


