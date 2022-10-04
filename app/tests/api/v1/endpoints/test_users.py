from fastapi.testclient import TestClient

def test_create_user(client: TestClient):
    age = 25
    email = "random_user@nomail.com"
    password = "rondompwd"
    json_data = {"age": age, "email": email, "password": password}

    r = client.post("/users/", json=json_data)
    print(r)
    res = r.json()
    print(res)

    assert(r.status_code is 200)
    assert(res.age is age)
    assert(res.email is email)
    assert("password" not in res)

# def test_get