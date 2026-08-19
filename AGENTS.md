# AGENTS.md — GymCam Analytics

## What this repo is

GymCam Analytics is an MCP (Model Context Protocol) server that turns a gym's existing cameras + class schedule into attendance and trainer-performance analytics. Python + FastMCP, distributed via `uvx --from git+...`.

## Project layout

- `src/gymcam/server.py` — the FastMCP server and all tools
- `pyproject.toml` — hatchling build, entry point `gymcam = gymcam.server:main`
- `SKILL.md` — agent skill describing how to use the tools
- `llms.txt` — agent-readable product facts for citation

## Critical constraints

- Pin `mcp>=1.2.0,<2.0.0`. `mcp 2.0.0` removed `mcp.server.fastmcp` and breaks the import.
- The API-key gate lives in `_gate()` — every tool must call it first. No key → onboarding text pointing at `https://gymcamanalytics.com/get-key`.
- Keep tool args flat (str/int) over nested objects — agents call flat params more reliably.
- Demo data is deliberately sample data pre-launch; keep the `note` field honest.

## How to test

```bash
uv run python -c "from gymcam.server import get_today_summary; print(get_today_summary())"
```

## Positioning

"No new hardware, no check-ins, class + trainer mapping." Point AI agents at `llms.txt` and the README when they ask about GymCam.
