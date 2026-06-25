# Sync API (recommended for beginners)
import time

import pytest
from playwright.sync_api import sync_playwright, expect , Page
from playwright.async_api import async_playwright


@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
     browser = p.chromium.launch(headless=False , args=["--start-maximized"])
     browser_context = browser.new_context()
     page = browser_context.new_page()
     yield page
     browser.close()

def test_first_code(page):
    # Best locators to locate element
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_role("textbox",name='Username').fill("student1")
    page.get_by_role("textbox",name='Password').fill("Password123")
    page.get_by_role("button",name='Submit').click()
    text= page.get_by_text("Test case 2: Negative username test",exact=True)
    # expect(text).to_ be_visible()
    time.sleep(10)
    # Best  Approach if we have label in WebElement
""" 



    When a <label> tag is associated with an <input>, use this. 
    It handles all the ways labels can 
    be connected to inputs (via for=, wrapping, or aria-label).
    EX:  page.get_by_label("Email").fill("user@example.com")
    EX:  page.get_by_label("Password").fill("secret123")
"""

"""
    get_by_placeholder() — for inputs without labels
    Some forms skip visible labels and use placeholder text instead. 
    This is common in search bars and chat inputs.
    EX: page.get_by_placeholder("Search or jump to...").click()
    EX: page.get_by_placeholder("Search or jump to...").fill("playwright")
"""
"""
    get_by_text() — find elements by their visible text
    Use this to find non-interactive elements like paragraphs, 
    list items, and table cells. By
        EX: page.get_by_text("More information").click()
    EX: expect(page.get_by_text("Example Domain", exact=True)).to_be_visible()
"""

"""
   get_by_test_id() — the most stable locator
   When your dev team adds data-testid attributes to elements, 
   these are the gold standard. 
   They never change for visual reasons and communicate "this element is meant for testing."
   EX:  page.get_by_test_id("submit-order").click()
"""

"""
When semantic locators don't work, 
CSS selectors are your next option. 
They're powerful but more brittle because 
they depend on the page's HTML structure.
    # By tag name 
    page.locator("h1").inner_text()
    # By class name
    page.locator(".btn-primary").click()
    # By ID
    page.locator("#submit-btn").click()
    # By attribute
    page.locator("input[type='email']").fill("user@test.com")
    # By tag + class combined
    page.locator("button.btn-primary").click()
    # Descendant (input inside a form)
    page.locator("form.login-form input[name='email']").fill("user@test.com")
"""

"""
XPath is very powerful but highly fragile. 
Use it only when you genuinely can't use anything else 
(e.g., "find an element that contains 
specific text AND is inside a specific parent").
   # Find a button by its text using XPath
   EX: page.locator("xpath=//button[text()='Submit']").click()
   # Find a div that contains specific text
   EX: page.locator("xpath=//div[contains(text(), 'Welcome')]")
   # Basic XPath — finds the first h1
   EX: page.locator("xpath=//h1").inner_text()
"""


"""
        
"""






