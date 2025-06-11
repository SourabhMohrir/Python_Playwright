import json
import time

import pytest
from playwright.sync_api import Page, expect, Playwright

from pageObjects.login import LoginPage


def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6841d8e881a2069530624378")


@pytest.mark.API
def test_redriectingToDifferentOrder(browserInstance, user_credentials):
    browserInstance.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",intercept_request)
    userName = user_credentials['userEmail']
    userPassword = user_credentials['userPassword']
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(userName, userPassword)
    orderHistory = dashboardPage.selectOrdersNavLink()
    orderHistory.clickOnFirstViewButton()
    expect(browserInstance.locator(".blink_me")).to_contain_text("You are not authorize to view this order")
