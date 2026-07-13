"""Integration test for API health endpoint."""

from fastapi.testclient import TestClient

from jol_analytics_ai.api.app import app


class TestHealthEndpoint:
    def test_health_returns_200(self) -> None:
        client = TestClient(app)
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
