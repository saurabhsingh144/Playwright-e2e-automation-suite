from playwright.sync_api import Page, expect
from playwright.async_api import async_playwright,expect
import pytest

def test_day_code_1(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    expect(page).to_have_title("Automation Testing Practice")

def test_day_code_2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

# @pytest.mark.asyncio
# async  def test_day_code_3():
#        async with async_playwright() as p:
#            ''' LAUNCH A BROWSER '''
#            browser = await p.chromium.launch(headless=False)
#            ''' CREATE A NEW PAGE '''
#            page=await browser.new_page()
#            await page.goto("https://automationexercise.com/test_cases")
#            my_url=page.url
#            expect(my_url).to_be("https://automationexercise.com/test_cases")





