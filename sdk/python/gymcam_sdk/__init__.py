"""GymCam Analytics SDK — official Python client for the GymCam REST API."""
from __future__ import annotations

import httpx

DEFAULT_BASE = "https://gymcamanalytics.com"


class GymCamClient:
    def __init__(self, api_key: str | None = None, base_url: str = DEFAULT_BASE, sandbox: bool = False):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.sandbox = sandbox

    def _headers(self) -> dict:
        h = {"Content-Type": "application/json"}
        if self.api_key:
            h["Authorization"] = f"Bearer {self.api_key}"
        if self.sandbox:
            h["X-Sandbox"] = "true"
        return h

    def _request(self, method: str, path: str) -> dict:
        r = httpx.request(method, f"{self.base_url}{path}", headers=self._headers())
        r.raise_for_status()
        return r.json()

    def status(self) -> dict:
        return self._request("GET", "/v1/status")

    def summary(self, gym_id: str = "demo") -> dict:
        return self._request("GET", f"/v1/summary?gym_id={gym_id}")

    def trainer_attendance(self, trainer: str, period: str = "week") -> dict:
        return self._request("GET", f"/v1/trainers/{trainer}?period={period}")

    def class_performance(self, limit: int = 8) -> dict:
        return self._request("GET", f"/v1/classes/performance?limit={limit}")

    def revenue_insights(self) -> dict:
        return self._request("GET", "/v1/revenue")
