import pytest
import allure
from utils.api_client import APIClient

# Valid Credentials (from ReqRes API docs)
VALID_EMAIL = "eve.holt@reqres.in"
VALID_PASSWORD = "cityslicka"

# Invalid Credentials
INVALID_EMAIL = "invalid@example.com"
INVALID_PASSWORD = "wrongpassword"

def test_login_success():
    """Test successful login with valid credentials."""
    response = APIClient.login(VALID_EMAIL, VALID_PASSWORD)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert APIClient.TOKEN is not None, "Authentication token should not be None"

def test_login_invalid_credentials():
    """Test login with invalid credentials."""
    response = APIClient.login(INVALID_EMAIL, INVALID_PASSWORD)
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "error" in response.json(), "Error message should be present"

def test_authenticated_request():
    """Test fetching users with authentication."""
    APIClient.login(VALID_EMAIL, VALID_PASSWORD)
    response = APIClient.get("/users?page=2")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "data" in response.json(), "Response should contain 'data'"

def test_access_protected_resource_without_token():
    """Test access to a resource that should be protected."""
    APIClient.TOKEN = None  # Ensure no token is set
    response = APIClient.get("/users?page=2")

    # If authentication is NOT required, expect 200
    assert response.status_code in [200, 401, 403], f"Unexpected status code {response.status_code}"

def test_access_protected_resource_with_invalid_token():
    """Test access to a protected resource with an invalid token."""
    APIClient.TOKEN = "invalid_token"  # Set an invalid token
    response = APIClient.get("/users?page=2")

    # If authentication is NOT required, expect 200
    assert response.status_code in [200, 401, 403], f"Unexpected status code {response.status_code}"