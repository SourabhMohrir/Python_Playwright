from .orderDetails import OrderDetailsPage


class OrderHistoryPage:
    def __init__(self, page):
        self.page = page

    def selectOrderById(self, orderId):
        latestOrder = self.page.locator("tr").filter(has_text=orderId)
        latestOrder.get_by_role("button", name="View").click()
        orderdetail = OrderDetailsPage(self.page)
        return orderdetail

