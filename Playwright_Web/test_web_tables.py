from playwright.sync_api import Page, expect
from pygments.lexer import words
import pytest

def test_static_web_tables(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    book_table=page.locator("table[name='BookTable'] tbody")
    expect(book_table).to_be_visible()
    # print(book_table.count())
    rows=book_table.locator("tr")
    header=rows.locator("th")
    second_rows = rows.nth(2).locator("td")
    all_rows=rows.all()
    print("Number of rows is :",rows.count())
    print("Number of columns is :",header.count())
    print("Number of second rows is :",second_rows.all_inner_texts())
    # print("Number of total rows is :", all_rows.count())
    expect(second_rows).to_have_text(['Learn Java', 'Mukesh', 'Java', '500'])
    all_row_data=rows.all()
    # for row in all_row_data[1:]:
    #     cols=row.locator('td').all_inner_texts()
    #     print(cols)
    sum = 0
    for row in all_row_data[1:]:
        author_name=row.locator('td').nth(1).inner_text()
        prices=row.locator('td').nth(3).inner_text()
        sum += int(prices)
    # print(author_name)
        if author_name == "Mukesh":
            print("Selected book is ",row.locator('td').nth(0).inner_text())
    print("Total price is ", sum)

def test_dynamic_web_tables(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table#google_vignette")
    book_table=page.locator("table.table tbody")
    rows=book_table.locator("tr").all()
    cpu_load=""
    for row in rows:
        process_name=row.locator("td").nth(0).inner_text()
        # print(process_name)
        if process_name == "Chrome":
            cpu_load=row.locator("td:has-text('%')").inner_text()
            print("Cpu load of chrome is",cpu_load)
            break
    expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)
    page.wait_for_timeout(5000)

def test_pagination_table(page:Page):
    page.goto("https://datatables.net/")
    # dropdown=page.locator("#dt-length-0")
    # dropdown.select_option(value="25")
    # print(dropdown.count())
    has_more_page=True
    while has_more_page:
        rows=page.locator("#example tbody tr").all()
        for row in rows:
            print(row.inner_text())
            with open("data.txt","a") as file:
                file.write(row.inner_text()+"\n")

        next_button=page.locator("button[aria-label='Next']")
        # next_button.click
        is_disabled=next_button.get_attribute("class")

        if "disabled" in is_disabled:
            has_more_page=False
        else:
            next_button.click()
def test_filter_validation(page:Page):
    page.goto("https://datatables.net/")
    options=["10","25","50"]
    for option in options:
      dropdown=page.locator("#dt-length-0")
      dropdown.select_option(label=option)
      rows = page.locator("#example tbody tr")
      print("Number of row filtered",rows.count())
      expect(rows).to_have_count(int(option))






