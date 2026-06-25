from playwright.sync_api import Page

def test_browserstack(page:Page):
    page.goto("https://bstackdemo.com/")

    dropdown=page.locator("//div[contains(text(),'Order by')]//select")
    dropdown.select_option(value="lowestprice")
    page.wait_for_timeout(5000)

    phone_title=page.locator("p.shelf-item__title")
    phone_text=[text for text in phone_title.all_inner_texts()]
    print(phone_text)

    price=page.locator("//div[@class='val']/b")
    price_text=[text.strip() for text in price.all_text_contents()]
    # print(phone_text[-1]



    for text in phone_text[-2:-1]:
        print(text)
    #
    # for price in price_text:
    #     print(price)
    #
    # price_sorted=sorted(price_text)
    # print(price_sorted)


