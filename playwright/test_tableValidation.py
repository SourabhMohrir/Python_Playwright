from playwright.sync_api import Page, Playwright, expect

def test_addToCart(page:Page):

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).text_content()=="Price":
            priceColumn = index
            break

    print(f"{index} index")
    riceRow = page.locator("tr").filter(has_text="Rice")
    priceOfRice = riceRow.locator("td").nth(priceColumn).text_content()
    assert priceOfRice == "37"
    print(f"Price of rice is {priceOfRice}")

