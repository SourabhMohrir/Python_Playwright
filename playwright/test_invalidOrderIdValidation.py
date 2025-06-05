import time

from playwright.sync_api import Page, expect

fakeResponse = {"data":[],"message":"No Orders"}

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6841d8e881a2069530624378")


def testNoOrdersInpage(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",intercept_request)
    page.get_by_placeholder("email@example.com").fill("srm@yahoo.com")
    page.get_by_placeholder("enter your passsword").fill("Sortest@123")
    page.locator(".login-btn").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    expect(page.locator(".blink_me")).to_contain_text("You are not authorize to view this order")
