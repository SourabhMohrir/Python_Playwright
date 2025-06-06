from .ordersHistory import OrderHistoryPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def selectOrdersNavLink(self):
        # Wait for the ORDERS button to be visible, then click it
        self.page.get_by_role("button", name="ORDERS").wait_for(state="visible", timeout=10000)
        self.page.get_by_role("button", name="ORDERS").click()
        orderHistoryPage = OrderHistoryPage(self.page)
        return orderHistoryPage

