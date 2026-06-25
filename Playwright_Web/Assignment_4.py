from playwright.sync_api import Page


def test_flipkart(page:Page):
    page.goto("https://www.flipkart.com/")
    search_box=page.locator("input[title='Search for Products, Brands and More']")
    search_box.nth(0).fill("smart")

    page.wait_for_timeout(5000)

    options=page.locator("ul>li")
    count=options.count()

    if count>5:
        print(options.nth(5).inner_text())

    for i in range(count):
        text = options.nth(i).inner_text()
        if text.strip().lower() == "smartphone":
            options.nth(i).click()
            break
    # print(count)
