import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
USER_ID = 1

@pytest.fixture
def session():
    """Общая HTTP-сессия для всех запросов теста"""
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json; charset=UTF-8"})
    yield s
    s.close()

# 1. GET - получить пользователя
def test_get_user(session):
    response = session.get(f"{BASE_URL}/users/{USER_ID}")

    # Проверка status code
    assert response.status_code == 200
    # Проверка, что ответ в формате JSON
    assert "application/json" in response.headers["Content-Type"]

    user = response.json()
    # Проверка структуры JSON
    expected_keys = {"id", "name", "username", "email", "address", "phone", "website", "company"}
    assert set(user.keys()) == expected_keys
    assert "city" in user["address"]
    assert "name" in user["company"]

    # Проверка значений полей
    assert user["id"] == USER_ID
    assert user["name"] == "Leanne Graham"
    assert "@" in user["email"]

    # Проверка времени ответа
    assert response.elapsed.total_seconds() < 2

# 2. GET - несуществующий пользователь (негативный сценарий)
def test_get_user_not_found(session):
    response = session.get(f"{BASE_URL}/users/9999")

    assert response.status_code == 404
    assert response.json() == {}

# 3. POST - создать пользователя
def test_create_user(session):
    new_user = {
        "name": "Andrey Tolmachev",
        "username": "atolmachev",
        "email": "tolmachev@test.ru",
    }
    response = session.post(f"{BASE_URL}/users", json=new_user)

    assert response.status_code == 201

    body = response.json()
    # Сервер должен вернуть id созданного пользователя
    assert "id" in body
    assert isinstance(body["id"], int)
    # Отправленные данные вернулись без изменений
    assert body["name"] == new_user["name"]
    assert body["username"] == new_user["username"]
    assert body["email"] == new_user["email"]

# 4. PUT - обновить пользователя
def test_update_user(session):
    updated_user = {
        "id": USER_ID,
        "name": "Andrey Updated",
        "username": "atolmachev",
        "email": "updated@test.ru",
    }
    response = session.put(f"{BASE_URL}/users/{USER_ID}", json=updated_user)

    assert response.status_code == 200

    body = response.json()
    assert body["id"] == USER_ID
    assert body["name"] == "Andrey Updated"
    assert body["email"] == "updated@test.ru"

# 5. Параметризованная проверка: у нескольких пользователей одинаковая структура
@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_users_have_same_structure(session, user_id):
    response = session.get(f"{BASE_URL}/users/{user_id}")

    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id
    assert isinstance(user["name"], str) and user["name"]
    assert isinstance(user["email"], str) and "@" in user["email"]
