import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright

load_dotenv()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser Selection"
    )

user_credentials_list = [
    {
        "userEmail": os.getenv("USER_EMAIL_1"),
        "userPassword": os.getenv("USER_PASSWORD_1")
    }]

@pytest.fixture(params=user_credentials_list,scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture
def browserInstance(playwright:Playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=True)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
