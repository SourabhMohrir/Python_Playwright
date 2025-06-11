#UI and API integrated test case
#Placing order using API and validating the order in UI
import json
import pytest
from playwright.sync_api import Playwright
from utils.apiBase import APIUtils
from pageObjects.login import LoginPage

# json file ->util->access into test

@pytest.mark.API
def test_e2e_web_api(playwright: Playwright, browserInstance, user_credentials):
    userName = user_credentials['userEmail']
    userPassword = user_credentials['userPassword']
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(userName, userPassword)
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    orderDetails = orderHistoryPage.selectOrderById(orderId)
    orderDetails.verifyMessage()

