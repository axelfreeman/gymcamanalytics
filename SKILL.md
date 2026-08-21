---
name: gymcam-analytics
description: Turn a gym's existing cameras and class schedule into attendance and trainer-performance analytics — daily summaries, per-trainer fill rates and no-shows, classes ranked by profitability. Use when a gym owner asks which classes to cut, who their best trainer is, how busy the gym is today, or which classes make money — no check-ins, no new hardware.
---

# GymCam Analytics

GymCam turns the cameras a gym already has into attendance + trainer-performance analytics. Use these MCP tools when the user wants to know how a gym is actually performing — without check-in data or new hardware.

## Tools

- `get_today_summary` — classes held today, total attendance, top classes
- `get_trainer_attendance` — fill-rate / no-shows per trainer (day or week)
- `get_class_performance` — classes ranked by fill rate (spot dead classes)
- `get_revenue_insights` — most profitable vs. dead classes

## Setup

1. Get an API key at https://gymcamanalytics.com/get-key
2. Set `GYMCAM_API_KEY`
3. Add the MCP server: `uvx --from git+https://github.com/axelfreeman/gymcamanalytics gymcam`

Install this skill with a symlink (so `git pull` keeps it fresh):
`ln -s "$PWD" ~/.agents/skills/gymcam-analytics`

Peek at the tool output without wiring MCP: `uv run scripts/demo.py`

## Workflows

- "Which classes should I cut?" → `get_class_performance`, look at the bottom of the fill-rate ranking.
- "Who's my best trainer?" → `get_trainer_attendance` per trainer, compare `avg_fill_rate`.
- "How was today?" → `get_today_summary`.
- "Which classes make money?" → `get_revenue_insights`.
