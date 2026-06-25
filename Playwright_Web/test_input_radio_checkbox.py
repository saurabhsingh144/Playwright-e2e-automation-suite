from playwright.sync_api import Page, expect
import pytest

def test_input_box(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    name=page.locator("input#name")

    # Check  textbox is visible or not
    expect(name).to_be_visible()
    expect(name).to_be_visible()
    #  Fill the value
    name.fill("Saurabh")
    page.wait_for_timeout(5000)
    #  Get the input value
    entered_value=name.input_value()
    print(entered_value)

    expect(name).to_have_attribute("placeholder","Enter Name")

def test_radio_button(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    male_radio=page.locator("input#male")
    #  CHECK MALE RADIO BUTTON SHOULD NOT BE CHECKED
    expect(male_radio).not_to_be_checked()

    # CHECK MALE RADIO BUTTON
    male_radio.check()

    # CHECK RADIO BUTTON IS CHECKED OR NOT
    expect(male_radio).to_be_checked()
    page.wait_for_timeout(5000)

    # female_radio=page.locator("input#female")

def test_checkboxes(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
#     # sunday_checkbox=page.get_by_label("sunday")
#     # expect(sunday_checkbox).not_to_be_checked()
#     # sunday_checkbox.click()
#     # expect(sunday_checkbox).to_be_checked()
#     # page.wait_for_timeout(5000)
#
# #   COUNT TOTAL NUMBER OF CHECKBOXES
    days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
#     checkboxes=[]
#     index=[1,4,6]
#     # Using list comprehension below is there
#     checkboxes=[page.get_by_label(day) for day in days]
#     for checkbox in checkboxes:
#         expect(checkbox).not_to_be_checked()
#         checkbox.check()
#         expect(checkbox).to_be_checked()
#
#     for checkbox in checkboxes[-3:]:
#         checkbox.uncheck()
#         page.wait_for_timeout(5000)
#
#     for checkbox in checkboxes:
#        if checkbox.is_checked():
#            checkbox.uncheck()
#            page.wait_for_timeout(2000)
#            expect(checkbox).not_to_be_checked()
#        elif not checkbox.is_checked():
#            checkbox.check()
#            page.wait_for_timeout(2000)
#            expect(checkbox).to_be_checked()
#        else:
#            checkbox.uncheck()
#
#     for i in index:
#         checkboxes[i].check()
#
    weekday=str(input("Enter the weekday"))

    for label in days:
        if label==weekday:
            checkbox=page.get_by_label(label)
            checkbox.check()



    # checkbox=[day for day in days]
    # print(checkbox[0])
    # for day in days[::-1]:
    #     checkbox=page.get_by_label(day)
    #     checkboxes.append(checkbox)
    #     expect(checkbox).not_to_be_checked()
    #     checkbox.check()
    #     page.wait_for_timeout(2000)
        # attribute=checkbox.get_attribute("name",)
        # print(attribute)
    # print(checkboxes)

def test_checkbox_count(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    checkboxes=page.locator("input[type='checkbox']")
    print(checkboxes.count())
    # expect(checkboxes).to_have_count(7)
    checkboxes_locators=checkboxes.all()

    for i in range(13):
         checkboxes_locators[i].check()







