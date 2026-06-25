import pytest
from playwright.sync_api import Page , expect

def test_bootstrap_dropdown(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # page.set_viewport_size({"width": 1920, "height": 1080})
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role(role="button",name="Login").click()
    page.wait_for_timeout(5000)
    page.locator("//span[text()='PIM']").click()
    page.wait_for_timeout(5000)
    # expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    page.locator("form i").nth(2).click()
    options=page.locator("div[role='listbox'] span")
    count=options.count()
    # expect(options).to_have_count(count)
    # print("Number of options",options.all_text_contents())
    # print(count)
    # job_titles=options.all_text_contents()
    #
    # for job_title in job_titles:
    #     print(job_title.strip())

    for i in range(count):
        text=options.nth(i).inner_text()
        print(text)
        if text=='Chief Executive Officer':
            options.nth(i).click()
            page.wait_for_timeout(5000)
            break
def test_comparison_methods(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    product=page.locator("h2.product-title")
 
    # print(product.nth(0).inner_text())
    # print(product.nth(0).text_content())
    for i in range(6):
        print(product.nth(i).text_content().strip())
        print(product.nth(i).inner_text())





