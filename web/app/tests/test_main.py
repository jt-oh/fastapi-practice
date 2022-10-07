from fastapi.testclient import TestClient

# TODO: 
# 1. configure test environment database
# 2. teardown/cleanup after each test case

def test_main(client: TestClient):
    r = client.get("/")

    assert(r.status_code is 200)

    root_res = r.json()
    print(root_res)
    assert(root_res["message"] == "Hello World")