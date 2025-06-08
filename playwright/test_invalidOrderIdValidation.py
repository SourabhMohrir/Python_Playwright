import json
import time

import pytest
from playwright.sync_api import Page, expect, Playwright

from pageObjects.login import LoginPage


def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6841d8e881a2069530624378")

with open('playwright/data/credentials.json') as f:
    test_data = json.load(f)
    user_credentials = test_data['user_credentials']

@pytest.mark.API
@pytest.mark.parametrize('user_credentials', user_credentials)
def test_redriectingToDifferentOrder(playwright: Playwright, browserInstance, user_credentials):
    browserInstance.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",intercept_request)
    userName = user_credentials['userEmail']
    userPassword = user_credentials['userPassword']
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(userName, userPassword)
    orderHistory = dashboardPage.selectOrdersNavLink()
    orderHistory.clickOnFirstViewButton()
    expect(browserInstance.locator(".blink_me")).to_contain_text("You are not authorize to view this order")
