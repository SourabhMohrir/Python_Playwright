#UI and API integrated test case
#Placing order using API and validating the order in UI
import json
import pytest
from playwright.sync_api import Playwright
from utils.apiBase import APIUtils
from pageObjects.login import LoginPage

# json file ->util->access into test
with open('playwright/data/credentials.json') as f:
    test_data = json.load(f)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.API
@pytest.mark.parametrize('user_credentials', user_credentials_list)
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

