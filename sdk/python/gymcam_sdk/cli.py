"""GymCam Analytics CLI — script gym interactions from the terminal."""
from __future__ import annotations

import argparse
import json
import os
import sys

from . import GymCamClient


def main() -> None:
    p = argparse.ArgumentParser(prog="gymcam", description="GymCam Analytics CLI")
    p.add_argument("--api-key", help="API key (or set GYMCAM_API_KEY)")
    p.add_argument("--sandbox", action="store_true", help="Run against sandbox sample data")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("status", help="Service status")

    sub.add_parser("summary", help="Today's summary")

    tp = sub.add_parser("trainers", help="Trainer fill rate + no-shows")
    tp.add_argument("trainer")
    tp.add_argument("--period", default="week", choices=["day", "week"])

    cp = sub.add_parser("classes", help="Classes ranked by fill rate")
    cp.add_argument("--limit", type=int, default=8)

    sub.add_parser("revenue", help="Most profitable vs. dead classes")

    args = p.parse_args()
    if not args.cmd:
        p.print_help()
        sys.exit(1)

    client = GymCamClient(api_key=args.api_key or os.environ.get("GYMCAM_API_KEY"), sandbox=args.sandbox)

    try:
        if args.cmd == "status":
            out = client.status()
        elif args.cmd == "summary":
            out = client.summary()
        elif args.cmd == "trainers":
            out = client.trainer_attendance(args.trainer, args.period)
        elif args.cmd == "classes":
            out = client.class_performance(args.limit)
        else:
            out = client.revenue_insights()
    except Exception as e:  # noqa: BLE001
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
