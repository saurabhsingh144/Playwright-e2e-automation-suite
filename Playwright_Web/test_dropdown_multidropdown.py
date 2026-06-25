from playwright.sync_api import Page, expect
import pytest

def test_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.set_viewport_size({"width": 1920, "height": 1080})
    # dropdown=page.locator("select#country")
    #  SELECT BY LABEL
    # dropdown.select_option("India")
    # SELECT BY VALUE
    # dropdown.select_option(value="Germany")
    # SELECT BY INDEX
    # dropdown
    # dropdown.select_option(index=2)
    # page.wait_for_timeout(2000)
    # CHECK TOTAL COUNT
    drop_down_option=page.locator("select#country>option")
    value=[text.strip() for text in drop_down_option.all_text_contents()]
    assert value[0]=="United States"
    print(value[0])
    # expect(count).to_have_count(10)
    # print(count.all_text_contents())
def test_multiple_option(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # BY LABEL
    # page.locator("#colors").select_option(["red","green"])
    # BY VALUE
    # page.locator("#colors").select_option(value=["blue","yellow"])
    #  BY INDEX
    # page.locator("#colors").select_option(index=[0,2])
    # page.locator("#colors").select_option(value="red")
    # CHECK TOTAL COUNT
    dropdown_option=page.locator("#colors>option")
    # expect(dropdown_option).to_have_count(7)
    option_text=[text.strip() for text in dropdown_option.all_text_contents()]
    original_list=option_text.copy()
    sorted_list=sorted(original_list)
    # assert original_list==sorted_list

    if original_list==sorted_list:
        print("The options are sorted correctly")
    else:
        print("The options are not sorted correctly")

    page.wait_for_timeout(5000)







