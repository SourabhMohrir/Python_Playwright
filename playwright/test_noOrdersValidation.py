from playwright.sync_api import Page, expect

fakeResponse = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(json=fakeResponse)


def testNoOrdersInpage(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)
    page.get_by_placeholder("email@example.com").fill("srm@yahoo.com")
    page.get_by_placeholder("enter your passsword").fill("Sortest@123")
    page.locator(".login-btn").click()
    page.get_by_role("button", name="ORDERS").click()
    expect(page.locator(".mt-4")).to_contain_text("You have No Orders to show at this time.  Please Visit Back Us")