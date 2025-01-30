import pytest
import allure
from utils.api_client import APIClient

def test_create_post():
    payload = {"title": "My New Post", "body": "This is a test post", "userId": 1}
    response = APIClient.post("/posts", payload)
    assert response.status_code == 201
    assert response.json()["title"] == "My New Post"

def test_get_all_posts():
    response = APIClient.get("/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0
def test_create_post_missing_fields():
    payload = {"title": "Missing body"}  # Missing 'body' and 'userId'
    response = APIClient.post("/posts", payload)
    
    assert response.status_code in [201, 400, 422], f"Unexpected status code {response.status_code}"
    assert "id" in response.json(), "Expected 'id' in response"

def test_create_post_with_invalid_data():
    payload = "invalid_data"  # Not JSON
    headers = {"Content-Type": "application/json"}  # Ensure correct format
    response = APIClient.post("/posts", payload, headers=headers)

    assert response is not None, "Response should not be None"
    assert response.status_code in [400, 422, 500], f"Unexpected status code {response.status_code}"

def test_delete_non_existent_post():
    """Test deleting a non-existent post."""
    post_id = 9999  # Assuming this ID doesn't exist
    response = APIClient.delete(f"/posts/{post_id}")

    assert response.status_code in [200, 204, 400, 404], f"Unexpected status code {response.status_code}"

