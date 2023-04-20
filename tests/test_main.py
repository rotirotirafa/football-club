from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_app():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        'Database': 'Status is up',
        'Application:': 'Status is up',
        'Networking': '0.99 ms latency'
    }