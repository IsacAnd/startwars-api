from unittest.mock import patch


@patch("app.routes.people.get_people")
def test_list_people_success(mock_get, client, auth_headers):
    mock_get.return_value = {
        "results": [
            {
                "name": "Luke Skywalker",
                "height": "172",
                "mass": "77",
                "gender": "male",
                "films": [],
                "url": "http://swapi.dev/api/people/1/"
            }
        ]
    }

    response = client.get("/people", headers=auth_headers)

    assert response.status_code == 200
    body = response.json()

    assert body["count"] == 1
    assert body["results"][0]["name"] == "Luke Skywalker"
    assert body["results"][0]["height"] == 172


@patch("app.routes.people.get_people")
def test_filter_people_by_name(mock_get, client, auth_headers):
    mock_get.return_value = {
        "results": [
            {"name": "Luke Skywalker", "gender": "male", "height": "172", "mass": "77", "films": [], "url": "x"},
            {"name": "Darth Vader", "gender": "male", "height": "202", "mass": "136", "films": [], "url": "y"}
        ]
    }

    response = client.get("/people?name=luke", headers=auth_headers)

    assert response.status_code == 200
    body = response.json()

    assert body["count"] == 1
    assert "luke" in body["results"][0]["name"].lower()


@patch("app.routes.people.get_people")
def test_sort_people_by_height(mock_get, client, auth_headers):
    mock_get.return_value = {
        "results": [
            {"name": "A", "height": "200", "mass": "90", "gender": "n/a", "films": [], "url": "x"},
            {"name": "B", "height": "150", "mass": "70", "gender": "n/a", "films": [], "url": "y"}
        ]
    }

    response = client.get("/people?sort=height", headers=auth_headers)

    body = response.json()
    heights = [p["height"] for p in body["results"]]

    assert heights == [150, 200]


def test_invalid_sort_field(client, auth_headers):
    response = client.get("/people?sort=banana", headers=auth_headers)
    assert response.status_code == 400


def test_missing_api_key(client):
    response = client.get("/people")
    assert response.status_code == 401
