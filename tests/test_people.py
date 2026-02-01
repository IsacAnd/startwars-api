from tests.conftest import client

def test_list_people():
    response = client.get("/people")
    assert response.status_code == 200
    body = response.json()
    assert "results" in body
    assert "count" in body

def test_filter_people_by_name():
    response = client.get("/people?name=luke")
    body = response.json()
    
    assert response.status_code == 200
    for p in body["results"]:
        assert "luke" in p["name"].lower()

def test_invalid_sort():
    response = client.get("/people?sort=banana")
    assert response.status_code == 400