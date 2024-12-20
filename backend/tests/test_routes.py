from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_setup():
    response = client.post(
        "/setup",
        data={"num_players": 3, "player_names": "Alice,Bob,Charlie", "rule": "strict"},
    )
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_get_backlog():
    response = client.get("/backlog")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    assert "backlog" in response.json()


def test_vote():
    response = client.post(
        "/vote", json={"task_id": "US001", "player": "Alice", "estimate": 5}
    )
    assert response.status_code == 200
    assert "message" in response.json() or "error" in response.json()


def test_validate():
    response = client.post("/validate", json={"task_id": "US001", "rule": "strict"})
    assert response.status_code == 200
    assert "validated" in response.json() or "error" in response.json()
