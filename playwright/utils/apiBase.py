from playwright.sync_api import Playwright

ordersPayload = {
    "orders": [
        {
            "country": "India",
            "productOrderedId": "67a8dde5c0d3e6622a297cc8"
        }
    ]
}

class APIUtils:

    def getToken(self,playwright:Playwright,user_credentials):
        userName = user_credentials['userEmail']
        userPassword = user_credentials['userPassword']
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post("api/ecom/auth/login",data={"userEmail": userName, "userPassword": userPassword},headers={"content-type": "application/json"})
        assert response.ok
        responseBody = response.json()
        token = responseBody['token']
        return token

    def createOrder(self, playwright:Playwright, user_credentials):
       token = self.getToken(playwright,user_credentials)
       api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
       response = api_request_context.post("api/ecom/order/create-order", data= ordersPayload,
                                headers={"Authorization":token, "Content-Type": "application/json"})
       responseBody = response.json()
       productOrderId = responseBody["orders"][0]
       return productOrderId

