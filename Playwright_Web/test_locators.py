# from playwright.async_api import expec
import re

from playwright.sync_api import Page,expect

def test_locators(page:Page):
    # page.goto("https://demo.nopcommerce.com/")
    ''' get_by_alt_text '''
    # page.wait_for_timeout(10)
    # expect(page.get_by_alt_text("Website for automation practice")).to_be_visible()
    '''CLOSE THE BROWSER INSTANCE'''
    # page.close()
    ''' get_by_text '''
    # expect(page.get_by_text("Welcome to our store")).to_be_visible()
    # expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible()

    ''' get_by_role'''
    # page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    # expect(page.get_by_role(role="heading",name="Register")).to_be_visible()

    ''' get_by_css_selector'''
    # page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    # page.wait_for_timeout(5000)
    # page.locator()

    '''get_xpath'''
    # page.goto("https://demowebshop.tricentis.com/")
    # product=page.locator("//h2//a[contains(@href,'computer')]")
    # product_titles= product.all_text_contents()
    # product_titles_last= product.last.text_content()
    # print(product_titles_last)
    # product_title_first= product.first.text_content()
    # print(product_title_first)
    # print(product_titles)
    # for i in product_titles:
    # facebook_link=page.locator("//div[@class='column follow-us']//li[@class='facebook']")
    # google_link=page.locator("//div[@class='column follow-us']//li[position()=5]")
    # expect(facebook_link).to_have_text("Facebook")
    # print(facebook_link)
    # expect(google_link).to_have_text("Google+")
    # print(google_link)
    # page.wait_for_timeout(3000)

    '''Dynamic Xpath'''
    page.goto("https://testautomationpractice.blogspot.com/")
    # button=page.locator("//button[text()='START' or text()='STOP' ]")
    button = page.locator("//button[@name='start' or @name='stop' ]")
    button.click()
    expect(button).to_have_text("STOP")
    # page.frame_locator()




    #     print(i)

    
    # num=[1,2,4]

    # square=[x*x  for x in num if x % 2 == 0]
    # print(square)











