#UI and API integrated test case
#Placing order using API and validating the order in UI
import time

from playwright.sync_api import Page, Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):


    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)

    #login to the application
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("srm@yahoo.com")
    page.get_by_placeholder("enter your passsword").fill("Sortest@123")
    page.locator(".login-btn").click()

    #Verify in order history -> order is placed
    page.get_by_role("button", name ="ORDERS").click()
    latestOrder = page.locator("tr").filter(has_text=orderId)
    latestOrder.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")






