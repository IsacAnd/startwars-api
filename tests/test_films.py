from unittest.mock import patch


@patch("app.routes.films.get_film")
@patch("app.routes.films.get_resource_by_url")
def test_film_characters_success(mock_resource, mock_film, client, auth_headers):
    mock_film.return_value = {
        "title": "A New Hope",
        "characters": [
            "url1",
            "url2"
        ]
    }

    mock_resource.side_effect = [
        {"name": "Luke Skywalker"},
        {"name": "Leia Organa"}
    ]

    response = client.get("/films/1/characters", headers=auth_headers)

    assert response.status_code == 200
    body = response.json()

    assert body["film"] == "A New Hope"
    assert body["count"] == 2
    assert body["characters"][0]["name"] == "Luke Skywalker"


@patch("app.routes.films.get_film")
def test_film_not_found(mock_film, client, auth_headers):
    mock_film.return_value = {"detail": "Not found"}

    response = client.get("/films/999/characters", headers=auth_headers)

    assert response.status_code == 404


def test_film_requires_auth(client):
    response = client.get("/films/1/characters")
    assert response.status_code == 401
