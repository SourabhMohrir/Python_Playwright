import json
import pytest
from playwright.sync_api import Page, expect, Playwright
from pageObjects.login import LoginPage

fakeResponse = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(json=fakeResponse)

@pytest.mark.API
def test_no_orders_in_page(browserInstance, user_credentials):
    userName = user_credentials['userEmail']
    userPassword = user_credentials['userPassword']
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    browserInstance.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)
    dashboardPage = loginPage.login(userName, userPassword)
    dashboardPage.selectOrdersNavLink()
    expect(browserInstance.locator(".mt-4")).to_contain_text("You have No Orders to show at this time. Please Visit Back Us")