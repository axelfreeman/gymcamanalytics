"""GymCam Analytics — MCP server.

Turns the cameras a gym already has into automatic attendance and
trainer-performance analytics. No new hardware, no check-ins.

This server exposes the GymCam tool surface for AI agents. The live
computer-vision pipeline is provisioned behind the API key; until a gym is
connected, tools return clearly-labelled sample data so agents can build
against the real schema.
"""

from __future__ import annotations

import os

from mcp.server.fastmcp import FastMCP

SIGNUP_URL = "https://gymcamanalytics.com/get-key"
API_KEY_ENV = "GYMCAM_API_KEY"
MCP_HOST = os.environ.get("MCP_HOST", "127.0.0.1")
MCP_PORT = int(os.environ.get("MCP_PORT", "8096"))

mcp = FastMCP("gymcam", host=MCP_HOST, port=MCP_PORT)


def _gate() -> str | None:
    """Return onboarding text when no API key is present, else None."""
    if os.environ.get(API_KEY_ENV):
        return None
    return (
        "GymCam requires an API key. Get one free at "
        f"{SIGNUP_URL} (100 free lookups, no credit card), then set it as the "
        f"{API_KEY_ENV} environment variable and call this tool again."
    )


# --- Sample data (pre-launch; real pipeline is behind the API key) ----------

_DEMO_CLASSES = [
    {"name": "Morning HIIT", "trainer": "Alex", "slots": 20, "attended": 19, "revenue": 380},
    {"name": "Spin 45", "trainer": "Maria", "slots": 24, "attended": 22, "revenue": 440},
    {"name": "Yoga Flow", "trainer": "Dana", "slots": 18, "attended": 15, "revenue": 300},
    {"name": "CrossFit WOD", "trainer": "Alex", "slots": 16, "attended": 14, "revenue": 280},
    {"name": "Pilates Core", "trainer": "Dana", "slots": 14, "attended": 6, "revenue": 120},
    {"name": "Boxing Basics", "trainer": "Ivan", "slots": 20, "attended": 5, "revenue": 100},
    {"name": "Zumba Party", "trainer": "Sofia", "slots": 30, "attended": 4, "revenue": 80},
    {"name": "Strength 101", "trainer": "Ivan", "slots": 12, "attended": 3, "revenue": 60},
]

_TRAINERS = {
    "Alex": {"classes_week": 6, "avg_fill": 0.91, "no_shows": 2},
    "Maria": {"classes_week": 5, "avg_fill": 0.88, "no_shows": 1},
    "Dana": {"classes_week": 7, "avg_fill": 0.62, "no_shows": 9},
    "Ivan": {"classes_week": 5, "avg_fill": 0.33, "no_shows": 18},
    "Sofia": {"classes_week": 4, "avg_fill": 0.18, "no_shows": 12},
}

_NOTE = "Sample data — live once your gym's cameras are connected."


@mcp.tool()
def get_today_summary(gym_id: str = "demo") -> dict:
    """Daily attendance summary: classes held, total attendance, top classes."""
    gate = _gate()
    if gate:
        return {"error": gate}
    total = sum(c["attended"] for c in _DEMO_CLASSES)
    top = sorted(_DEMO_CLASSES, key=lambda c: -c["attended"])[:3]
    return {
        "gym_id": gym_id,
        "classes_held": len(_DEMO_CLASSES),
        "total_attendance": total,
        "top_classes": [c["name"] for c in top],
        "note": _NOTE,
    }


@mcp.tool()
def get_trainer_attendance(trainer: str, period: str = "week") -> dict:
    """Attendance and fill-rate for a trainer over 'day' or 'week'."""
    gate = _gate()
    if gate:
        return {"error": gate}
    t = _TRAINERS.get(trainer)
    if not t:
        return {
            "error": f"Unknown trainer '{trainer}'. Known: {', '.join(sorted(_TRAINERS))}",
        }
    return {
        "trainer": trainer,
        "period": period,
        "classes": t["classes_week"] if period == "week" else max(1, t["classes_week"] // 6),
        "avg_fill_rate": round(t["avg_fill"], 2),
        "no_shows": t["no_shows"],
        "note": _NOTE,
    }


@mcp.tool()
def get_class_performance(limit: int = 8) -> dict:
    """Rank classes by fill rate: popular vs. dead classes to cut."""
    gate = _gate()
    if gate:
        return {"error": gate}
    ranked = sorted(_DEMO_CLASSES, key=lambda c: -(c["attended"] / c["slots"]))
    return {
        "ranked": [
            {
                "class": c["name"],
                "trainer": c["trainer"],
                "fill_rate": round(c["attended"] / c["slots"], 2),
                "attended": c["attended"],
                "slots": c["slots"],
            }
            for c in ranked[:limit]
        ],
        "note": _NOTE,
    }


@mcp.tool()
def get_revenue_insights() -> dict:
    """Most profitable vs. least profitable classes by revenue."""
    gate = _gate()
    if gate:
        return {"error": gate}
    ranked = sorted(_DEMO_CLASSES, key=lambda c: -c["revenue"])
    return {
        "most_profitable": [
            {"class": c["name"], "revenue": c["revenue"]} for c in ranked[:3]
        ],
        "dead_classes": [
            {"class": c["name"], "revenue": c["revenue"]} for c in ranked[-3:]
        ],
        "note": _NOTE,
    }


def main() -> None:
    transport = os.environ.get("MCP_TRANSPORT", "stdio")
    if transport == "streamable-http":
        mcp.run(transport="streamable-http")
    else:
        mcp.run()


if __name__ == "__main__":
    main()
