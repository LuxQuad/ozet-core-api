from lib2to3.pgen2 import token
from fastapi.testclient import TestClient

from app.main import service
from app.settings import settings

import json
from urllib.parse import urlencode

client = TestClient(service)


def test_create_user(is_testcase=True):
    headers = {'Content-Type': 'application/json'}

    form_data = {
        "email": "ozet@ozet.me",
        "username": "ozet",
        "password": "ozetozet"
    }

    response = client.post("/users", data=json.dumps(form_data), headers=headers)

    if response.status_code == 400:
        assert response.status_code == 400
        assert response.json() == {"detail": "Username already registered"}
    else:
        assert response.status_code == 200
        #assert response.json() == test_data


def test_login_user(is_testcase=True):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    form_data = {
        "username": "tests",
        "password": "testest"
    }

    response = client.post("/users/token", data=urlencode(form_data), headers=headers)

    if is_testcase:
        assert response.status_code == 200

    return response.json()


def test_get_user(is_testcase=True):
    token_key = test_login_user(is_testcase=False)['access_token']

    headers = {
        "Authorization": f"Bearer {token_key}",
    }

    response = client.get("/users", headers=headers)

    assert response.status_code == 200


def test_get_user(is_testcase=True):
    token_key = test_login_user(is_testcase=False)['access_token']

    headers = {
        "Authorization": f"Bearer {token_key}",
    }

    response = client.get("/users/items", headers=headers)

    assert response.status_code == 200
