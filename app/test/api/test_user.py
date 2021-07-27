from fastapi.testclient import TestClient

from app.main import service
from app.settings import settings

client = TestClient(service)


def test_read_user():
    response = client.get("/users", headers={"X-Token": settings.X_TOKEN})

    assert response.status_code == 200