from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)


def test_should_return_200_with_valid_input():
    response = client.post(
        "/api/evaluation/url", json={"url": "https://www.google.com"}
    )

    assert response.status_code == status.HTTP_200_OK


def test_should_return_response():
    response = client.post(
        "/api/evaluation/url",
        json={"url": "https://www.google.com"},
    )

    assert response.json() == {
        "elements_evaluated_count": 0,
        "errors_found_count": 0,
        "results_details": [],
    }


def test_should_return_422_with_no_input():
    response = client.post("/api/evaluation/url")

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_should_return_422_with_invalid_input():
    response = client.post("/api/evaluation/url", json={"u": ""})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_should_return_400_with_invalid_url():
    response = client.post("/api/evaluation/url", json={"url": "google"})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
