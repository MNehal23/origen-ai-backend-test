# part_a/tests/test_api.py
import asyncio
import os
import pytest
from fastapi.testclient import TestClient

# import the app from your project
from app.main import app

client = TestClient(app)

@pytest.fixture(scope="session", autouse=True)
def ensure_db_env():
    # Ensure DATABASE_URL is set for tests (point to your dev DB). You can also mock DB in future.
    if "DATABASE_URL" not in os.environ:
        os.environ["DATABASE_URL"] = "postgresql://postgres:postgres@localhost:5432/origen"
    # Let any startup events run
    # Note: TestClient will start/stop the app on first request automatically.
    yield

def test_list_machines():
    resp = client.get("/api/machines")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "name" in data[0]

def test_create_and_get_simulation():
    # create a simulation (use an existing machine id, commonly 1)
    payload = {"name": "pytest-sim", "machine_id": 1}
    resp = client.post("/api/simulations", json=payload)
    assert resp.status_code == 200 or resp.status_code == 201
    sim = resp.json()
    assert sim["name"] == payload["name"]
    sim_id = sim["id"]

    # fetch detail
    resp2 = client.get(f"/api/simulations/{sim_id}")
    assert resp2.status_code == 200
    detail = resp2.json()
    assert detail["id"] == sim_id
    assert "convergence" in detail
