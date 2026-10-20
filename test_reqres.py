import requests

BASE_URL = "https://reqres.in/api"


def test_get_user():
    response = requests.get(f"{BASE_URL}/users/2")
    json_data = response.json()

    assert response.status_code == 200

    assert "data" in json_data

    assert json_data["data"]["id"] == 2

    assert json_data["data"]["email"] == "janet.weaver@reqres.in"

    assert response.elapsed.total_seconds() * 1000 < 1000


def test_create_user():
    payload = {
        "name": "Иван",
        "job": "Тестировщик"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    json_data = response.json()

    assert response.status_code == 201

    assert json_data["name"] == "Иван"

    assert json_data["job"] == "Тестировщик"

    assert "id" in json_data
    assert isinstance(json_data["id"], str) # В reqres.in ID приходит строкой

    assert "createdAt" in json_data


def test_update_user():
    payload = {
        "name": "Иван Обновленный",
        "job": "Senior QA"
    }
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    json_data = response.json()

    assert response.status_code == 200

    assert json_data["name"] == "Иван Обновленный"

    assert json_data["job"] == "Senior QA"

    assert "updatedAt" in json_data

    assert response.elapsed.total_seconds() * 1000 < 2000