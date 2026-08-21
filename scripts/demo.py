#!/usr/bin/env python3
"""GymCam demo — exercise all four tools without wiring the MCP server.

Run:  uv run scripts/demo.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
os.environ.setdefault("GYMCAM_API_KEY", "demo")  # show sample data

from gymcam.server import (  # noqa: E402
    get_today_summary,
    get_trainer_attendance,
    get_class_performance,
    get_revenue_insights,
)


def show(title: str, data: dict) -> None:
    print(f"\n### {title}")
    print(json.dumps(data, indent=2, ensure_ascii=False))


show("Today's summary", get_today_summary())
show("Trainer 'Alex' (week)", get_trainer_attendance("Alex", "week"))
show("Class performance (top 5)", get_class_performance(limit=5))
show("Revenue insights", get_revenue_insights())
