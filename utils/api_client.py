import requests
import allure

class APIClient:
    BASE_URL = "https://reqres.in/api"
    TOKEN = None  # Store authentication token

    @staticmethod
    @allure.step("Login with email: {username}")
    def login(username, password):
        """Authenticate and store the token"""
        payload = {"email": username, "password": password}
        response = requests.post(f"{APIClient.BASE_URL}/login", json=payload)

        with allure.step("Request Payload:"):
            allure.attach(str(payload), name="Payload", attachment_type=allure.attachment_type.JSON)
        
        with allure.step("Response:"):
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        if response.status_code == 200:
            APIClient.TOKEN = response.json().get("token")
        return response

    @staticmethod
    def get_headers():
        """Return authorization headers if logged in"""
        headers = {"Content-Type": "application/json"}
        if APIClient.TOKEN:
            headers["Authorization"] = f"Bearer {APIClient.TOKEN}"
        return headers

    @staticmethod
    @allure.step("Sending GET request to {endpoint}")
    def get(endpoint, params=None):
        response = requests.get(f"{APIClient.BASE_URL}{endpoint}", params=params, headers=APIClient.get_headers())

        with allure.step("Response Details:"):
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        return response

    @staticmethod
    @allure.step("Sending POST request to {endpoint}")
    def post(endpoint, data, headers=None):
        final_headers = APIClient.get_headers()
        if headers:
            final_headers.update(headers)
        response = requests.post(f"{APIClient.BASE_URL}{endpoint}", json=data, headers=final_headers)

        with allure.step("Request Payload:"):
            allure.attach(str(data), name="Payload", attachment_type=allure.attachment_type.JSON)
        
        with allure.step("Response:"):
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        return response
