import pytest
import allure
from utils.api_client import APIClient

VALID_EMAIL = "eve.holt@reqres.in"
VALID_PASSWORD = "cityslicka"

def test_get_all_users():
    response = APIClient.get("/users")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_user_by_id():
    """Test getting a user by ID."""
    user_id = 1
    response = APIClient.get(f"/users/{user_id}")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    json_response = response.json()
    assert "data" in json_response, f"Response does not contain 'data': {json_response}"

    user_data = json_response["data"]  # Extract the user object
    assert "id" in user_data, f"Response does not contain 'id': {user_data}"
    assert user_data["id"] == user_id, f"Expected user ID {user_id}, got {user_data['id']}"

def test_get_non_existent_user():
    user_id = 9999  # Assuming this ID does not exist
    response = APIClient.get(f"/users/{user_id}")

    assert response is not None, "Response should not be None"
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"
def test_get_users_with_auth():
    """Test fetching users with authentication."""
    APIClient.login(VALID_EMAIL, VALID_PASSWORD)
    response = APIClient.get("/users?page=2")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "data" in response.json(), "Response should contain 'data'"

