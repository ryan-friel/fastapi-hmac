from fastapi.testclient import TestClient
import json

from main import app

client = TestClient(app)


def test_root():
    """
    Test the root path.
    Just to make sure that the simple get request is working appropriately.
    This should always pass.
    """
    response = client.get("/")

    client.post

    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to my demo!"}


def test_generate_token():
    """
    Test the generate token endpoint.
    Should return true.
    """
    response = client.post("/generate-token", json={'name': 'ryan'})
    assert response.status_code == 200
    json_object: dict = json.loads(response.json())
    assert json_object == {
        "name": "ryan",
        "signature": "ecb2aac0bc4b171c9a865a66abfdb3e8e21893523271fe793dda198a54251553"
    }


def test_int_generate_token():
    """
    Test the generate token endpoint.
    Should return false. Testing with an integer.
    """
    response = client.post("/generate-token", json=1)
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Invalid JSON"
    }


def test_string_generate_token():
    """
    Test the generate token endpoint.
    Should return false. Testing with a non-json string.
    """
    response = client.post("/generate-token", json="one")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Invalid JSON"
    }