from fastapi.testclient import TestClient

test_user_data = [
    {"email": "tom@nomail.com", "password": "tompwd", "age": 28},
    {"email": "tina@nomail.com", "password": "tinapwd", "age": 38},
    {"email": "jack@nomail.com", "password": "jackpwd", "age": 17},
    {"email": "sandy@nomail.com", "password": "sandypwd", "age": 21},
    {"email": "brian@nomail.com", "password": "brianpwd", "age": 50},
    {"email": "kelly@nomail.com", "password": "kellypwd", "age": 35}
]

def test_create_user(client: TestClient, configure_test_db):
    user_data = test_user_data[0]

    r = client.post("/users/", json=user_data)
    res = r.json()

    assert(r.status_code is 200)
    assert(res["age"] is user_data["age"])
    assert(res["email"] == user_data["email"])
    assert("password" not in res)

# def test_get