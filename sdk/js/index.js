/**
 * GymCam Analytics SDK — official JavaScript client for the GymCam REST API.
 * @module @gymcam/sdk
 */

const DEFAULT_BASE = "https://gymcamanalytics.com";

class GymCamClient {
  constructor({ apiKey, baseUrl = DEFAULT_BASE, sandbox = false } = {}) {
    this.apiKey = apiKey;
    this.baseUrl = baseUrl.replace(/\/$/, "");
    this.sandbox = sandbox;
  }

  async _request(path, { method = "GET" } = {}) {
    const headers = { "Content-Type": "application/json" };
    if (this.apiKey) headers.Authorization = `Bearer ${this.apiKey}`;
    if (this.sandbox) headers["X-Sandbox"] = "true";
    const res = await fetch(`${this.baseUrl}${path}`, { method, headers });
    if (!res.ok) {
      const err = new Error(`GymCam API ${res.status}: ${await res.text()}`);
      err.status = res.status;
      throw err;
    }
    return res.json();
  }

  status() {
    return this._request("/v1/status");
  }

  summary(gymId = "demo") {
    return this._request(`/v1/summary?gym_id=${encodeURIComponent(gymId)}`);
  }

  trainerAttendance(trainer, period = "week") {
    return this._request(`/v1/trainers/${encodeURIComponent(trainer)}?period=${encodeURIComponent(period)}`);
  }

  classPerformance(limit = 8) {
    return this._request(`/v1/classes/performance?limit=${encodeURIComponent(limit)}`);
  }

  revenueInsights() {
    return this._request("/v1/revenue");
  }
}

module.exports = { GymCamClient, DEFAULT_BASE };
