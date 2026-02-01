from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

client.get("/people", headers={"x-api-key": "starwars-secret-key"})