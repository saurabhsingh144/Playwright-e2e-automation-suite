
from playwright.sync_api import Page
def test_css_selector(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    css_locators =page.locator("h2>a[href *='computer']")
    print(css_locators)
    count = css_locators.count()
    print(count)


def test_links_selector(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    first_link=page.locator("div.follow-us > ul > *:first-child>a")
    second_link=page.locator("div.follow-us > ul > *:last-child>a")
    print(first_link)
    print(second_link)



