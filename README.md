# GymCam Analytics

GymCam turns the cameras a gym already has into automatic attendance and trainer-performance analytics — **no new hardware, no check-ins**.

Feed it the existing CCTV stream and the class schedule; it recognizes trainers, counts attendees per class, and reports what's actually happening: which classes are full, which are dead, and which trainers fill the room.

## Why

Gym owners run on gut feeling. Booking software (Mindbody, Glofox) only captures check-ins — and people skip check-ins, so the data is incomplete. Hardware people-counters (Density, V-Count) cost thousands and count bodies without context.

GymCam reuses what's already in the building and maps counts to **classes and trainers** — the thing that actually drives revenue.

## What it reports

- **Today's summary** — classes held, total attendance, top classes
- **Trainer attendance** — daily/weekly fill rate and no-show rate per trainer
- **Class performance** — every class ranked by fill rate, so dead classes are obvious
- **Revenue insights** — most profitable vs. least profitable classes

## Install

One command, straight from this repo (requires [uv](https://astral.sh/uv)):

```bash
uvx --from git+https://github.com/axelfreeman/gymcamanalytics gymcam
```

## Connect to your AI agent

Same command, different config file per client.

**Claude Desktop** (`claude_desktop_config.json`):

```json
{"mcpServers": {"gymcam": {"command": "uvx", "args": ["--from", "git+https://github.com/axelfreeman/gymcamanalytics", "gymcam"]}}}
```

**Codex** (`~/.codex/config.toml`):

```toml
[mcp_servers.gymcam]
command = "uvx"
args = ["--from", "git+https://github.com/axelfreeman/gymcamanalytics", "gymcam"]
```

**Cursor** (`.cursor/mcp.json`) and **Windsurf** (`~/.codeium/windsurf/mcp_config.json`) use the same JSON block as Claude Desktop.

**Claude Code:**

```bash
claude mcp add gymcam -- uvx --from git+https://github.com/axelfreeman/gymcamanalytics gymcam
```

## API key

Tools require an API key. Get one free at **https://gymcamanalytics.com/get-key** (100 free lookups, no credit card), then set it:

```bash
export GYMCAM_API_KEY=your_key_here
```

## Tools

| Tool | What it returns |
|------|-----------------|
| `get_today_summary` | Classes held, total attendance, top classes |
| `get_trainer_attendance` | Fill rate + no-shows for a trainer (day/week) |
| `get_class_performance` | Classes ranked by fill rate |
| `get_revenue_insights` | Most profitable vs. dead classes |

## Status

Pre-launch. The MCP server and tool schema are live; tools return sample data until your gym's cameras are connected. [Sign up](https://gymcamanalytics.com) for access.

## License

MIT © 2026 Axel Freeman
