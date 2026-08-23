"""GymCam Analytics — documentation MCP server.

A separate MCP surface for answering questions from the GymCam docs, so agents
can 'learn' (pull docs) over the same protocol they use to 'do' (the product MCP
server). Streamable HTTP when MCP_TRANSPORT=streamable-http.
"""
from __future__ import annotations

import os

from mcp.server.fastmcp import FastMCP

MCP_HOST = os.environ.get("MCP_HOST", "127.0.0.1")
MCP_PORT = int(os.environ.get("MCP_PORT", "8099"))

mcp = FastMCP("gymcam-docs", host=MCP_HOST, port=MCP_PORT)

_DOCS = {
    "overview": "GymCam Analytics turns a gym's existing cameras (CCTV/RTSP) and class schedule into attendance and trainer-performance analytics — no new hardware, no check-ins. Outputs: daily class summaries, per-trainer fill rate and no-shows, classes ranked by occupancy, and revenue insights.",
    "api": "REST API at https://gymcamanalytics.com. Endpoints: GET /v1/summary (today's summary), GET /v1/trainers/{trainer} (fill rate + no-shows, period=day|week), GET /v1/classes/performance (classes ranked by fill rate), GET /v1/revenue (most profitable vs dead classes). OpenAPI: /openapi.json. Auth: Authorization: Bearer <api-key>.",
    "auth": "Get a free API key at https://gymcamanalytics.com/get-key (100 free lookups, no credit card). Send it as Authorization: Bearer <api-key>. Auth metadata: /.well-known/oauth-protected-resource (RFC 9728) and /.well-known/oauth-authorization-server (RFC 8414).",
    "mcp": "GymCam ships as an MCP server. Install: uvx --from git+https://github.com/axelfreeman/gymcamanalytics gymcam. Hosted endpoint: https://gymcamanalytics.com/mcp (streamable HTTP). Tools: get_today_summary, get_trainer_attendance, get_class_performance, get_revenue_insights.",
    "pricing": "Free developer API key (100 free lookups). Paid plans are per-location SaaS for gyms, starting once a gym's cameras are connected.",
    "sandbox": "Add the X-Sandbox: true header to exercise the API against sample data without touching production.",
}

_TOPICS = ", ".join(sorted(_DOCS))


@mcp.tool()
def read_doc(topic: str) -> str:
    """Read GymCam documentation. topic is one of: overview, api, auth, mcp, pricing, sandbox."""
    t = (topic or "").strip().lower()
    if t not in _DOCS:
        return f"Unknown topic '{topic}'. Available: {_TOPICS}."
    return _DOCS[t]


@mcp.tool()
def list_docs() -> str:
    """List available documentation topics."""
    return _TOPICS


def main() -> None:
    transport = os.environ.get("MCP_TRANSPORT", "stdio")
    if transport == "streamable-http":
        mcp.run(transport="streamable-http")
    else:
        mcp.run()


if __name__ == "__main__":
    main()
