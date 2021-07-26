from fastapi.testclient import TestClient

from app.main import service

client = TestClient(service)


def test_read_main():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "live"}
