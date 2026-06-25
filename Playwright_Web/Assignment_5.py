from playwright.sync_api import Page, expect

import pytest
import re
def test_dynamic_table_ass(page: Page):
     page.goto("https://testautomationpractice.blogspot.com/")
     body=page.locator("table#taskTable tbody ")
     rows=body.locator("tr").all()
     # print(rows)
     # cpu_load=""
     for row in rows:
         cols=row.locator("td").nth(0).inner_text()
         if cols=="Chrome":
             cpu_load=row.locator("td:has-text('%')").inner_text()
             network_load=row.locator("td").filter(
                 has_text=re.compile("Mbps$")
             ).inner_text()
             print(network_load)
             displayed_cpu_load=page.locator("#displayValues")
             expect(displayed_cpu_load).to_contain_text(cpu_load)
             expect(displayed_cpu_load).to_contain_text(network_load)

             print(cpu_load)
         if cols=="Firefox":
             memory_usage=row.locator("td").filter(
                 has_text=re.compile("MB$")
             ).inner_text()
             displayed_cpu_load = page.locator("#displayValues")
             expect(displayed_cpu_load).to_contain_text(memory_usage)
             print(memory_usage)

from playwright.sync_api import Page

def test_paginated_table(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    body = page.locator("#productTable tbody")

    n = 4
    for i in range(1, n + 1):

        # print rows from current page

        # click pagination button
        if i >1:
          next_button = page.locator("ul#pagination li a").filter(
            has_text=f"{i}"
          )
          next_button.click()
        print(f"\n--- Page {i} ---")
        rows = body.locator("tr").all()
        for row in rows:
            print(row.inner_text())

def test_blaze_website(page: Page):
    page.goto("https://blazedemo.com/")
    drop_from=page.locator("select[name='fromPort']")
    drop_from.select_option(label='Boston')
    drop_to=page.locator("select[name='toPort']")
    drop_to.select_option(label='London')
    page.get_by_role(role="button",name="Find Flights").click()

    body=page.locator("table.table tbody")
    rows=body.locator("tr").all()
    price_list=[]
    for row in rows:
        prices=row.locator("td").nth(5).inner_text()
        # flights=row.locator("td").nth(2).inner_text()
        price_list.append(float(prices.replace("$","")))
        # print(flights)
        # print(prices)
    sorted_price=sorted(price_list)
    print("shorted price is ",sorted_price)
    min_price=min(sorted_price)
    for row in rows:
        prices=row.locator("td").nth(5).inner_text()
        if float(prices.replace("$",""))==min_price:
            navigate=row.locator('td input[type="submit"]')
            navigate.click()
            break
    page.wait_for_timeout(5000)







    from playwright.sync_api import Page



    # ul  # pagination  li




