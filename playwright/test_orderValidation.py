import time

from playwright.sync_api import Page, Playwright, expect

def test_addToCart(page:Page):
    #select iphonex and nokia edge add to card
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone x")
    iphoneProduct.get_by_role("button", name="add").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button", name="add").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    expect(page.get_by_text("iphone X")).to_be_visible()
    expect(page.get_by_text("Nokia Edge")).to_be_visible()