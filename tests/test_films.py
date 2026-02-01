from tests.conftest import client

def test_film_characters():
    response = client.get("/films/1/characters")
    assert response.status_code == 200
    body = response.json()
    assert "characters" in body
    assert body["count"] > 0
