from playwright.sync_api import Playwright

ordersPayload = {
    "orders": [
        {
            "country": "India",
            "productOrderedId": "67a8dde5c0d3e6622a297cc8"
        }
    ]
}
loginPayload = {"userEmail": "srm@yahoo.com", "userPassword": "Sortest@123"}

class APIUtils:

    def getToken(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post("api/ecom/auth/login",data=loginPayload,headers={"content-type": "application/json"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        token = responseBody['token']
        return token

    def createOrder(self, playwright:Playwright):
       token = self.getToken(playwright)
       api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
       response = api_request_context.post("api/ecom/order/create-order", data= ordersPayload,
                                headers={"Authorization":token, "Content-Type": "application/json"})
       print(response.json())
       responseBody = response.json()
       productOrderId = responseBody["orders"][0]
       return productOrderId

