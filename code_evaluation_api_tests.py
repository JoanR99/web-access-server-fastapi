from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)


def test_should_return_200_with_valid_input():
    response = client.post("/api/evaluation/code", json={"code": "<html></html>"})

    assert response.status_code == status.HTTP_200_OK


def test_should_return_response():
    response = client.post(
        "/api/evaluation/code",
        json={"code": "<html><head><title>title</title></head></html>"},
    )

    assert response.json() == {
        "elements_evaluated_count": 1,
        "errors_found_count": 1,
        "results_details": [{"element_count": 1, "error_count": 1, "test_name": "H57"}],
    }


def test_should_return_422_with_no_input():
    response = client.post("/api/evaluation/code")

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_should_return_422_with_invalid_input():
    response = client.post("/api/evaluation/code", json={"co": ""})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
