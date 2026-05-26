#!/usr/bin/env python3

import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
LOG_PATH = ROOT / ".codex-memory" / "maintenance-log.json"
DEFAULT_INTERVAL_DAYS = 7
MAX_HISTORY = 20


def now_local() -> datetime:
    return datetime.now().astimezone()


def now_iso() -> str:
    return now_local().isoformat(timespec="seconds")


def default_log() -> dict:
    return {
        "version": 1,
        "maintenance_interval_days": DEFAULT_INTERVAL_DAYS,
        "last_checked_at": None,
        "last_maintenance_at": None,
        "last_maintenance_note": "",
        "history": [],
    }


def load_log() -> dict:
    if not LOG_PATH.exists():
        return default_log()

    with LOG_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    merged = default_log()
    merged.update(data)
    if not isinstance(merged.get("history"), list):
        merged["history"] = []
    return merged


def save_log(data: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def append_history(data: dict, event_type: str, note: str) -> None:
    history = data.setdefault("history", [])
    history.append(
        {
            "at": now_iso(),
            "type": event_type,
            "note": note.strip(),
        }
    )
    data["history"] = history[-MAX_HISTORY:]


def build_status(data: dict) -> dict:
    interval_days = int(data.get("maintenance_interval_days", DEFAULT_INTERVAL_DAYS))
    current_time = now_local()
    last_maintenance = parse_iso(data.get("last_maintenance_at"))

    if last_maintenance is None:
        overdue = True
        days_since = None
        next_due = None
    else:
        delta = current_time - last_maintenance
        days_since = round(delta.total_seconds() / 86400, 2)
        overdue = delta >= timedelta(days=interval_days)
        next_due = (last_maintenance + timedelta(days=interval_days)).isoformat(timespec="seconds")

    return {
        "interval_days": interval_days,
        "last_checked_at": data.get("last_checked_at"),
        "last_maintenance_at": data.get("last_maintenance_at"),
        "last_maintenance_note": data.get("last_maintenance_note", ""),
        "history_count": len(data.get("history", [])),
        "days_since_maintenance": days_since,
        "next_due_at": next_due,
        "overdue": overdue,
    }


def print_status(status: dict) -> None:
    print("Maintenance status")
    print("- Log file: .codex-memory/maintenance-log.json")
    print(f"- Interval days: {status['interval_days']}")
    print(f"- Last checked at: {status['last_checked_at'] or 'never'}")
    print(f"- Last maintenance at: {status['last_maintenance_at'] or 'never'}")
    print(f"- Last maintenance note: {status['last_maintenance_note'] or '-'}")
    print(f"- History entries kept: {status['history_count']}")
    if status["days_since_maintenance"] is None:
        print("- Days since maintenance: unknown")
    else:
        print(f"- Days since maintenance: {status['days_since_maintenance']}")
    print(f"- Next due at: {status['next_due_at'] or 'now'}")
    print(f"- Overdue: {'yes' if status['overdue'] else 'no'}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Read or update the local maintenance log for this Codex project."
    )
    parser.add_argument("--record-check", action="store_true", help="Update last_checked_at.")
    parser.add_argument(
        "--record-maintenance",
        action="store_true",
        help="Update maintenance timestamp and append a maintenance history event.",
    )
    parser.add_argument("--note", default="", help="Optional note stored with the maintenance event.")
    parser.add_argument(
        "--set-interval-days",
        type=int,
        help="Override maintenance interval in days.",
    )
    parser.add_argument("--quiet", action="store_true", help="Do not print human-readable status output.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    data = load_log()
    changed = False

    if args.set_interval_days is not None:
        data["maintenance_interval_days"] = max(1, args.set_interval_days)
        changed = True

    if args.record_check:
        data["last_checked_at"] = now_iso()
        changed = True

    if args.record_maintenance:
        timestamp = now_iso()
        note = args.note.strip() or "Routine project maintenance"
        data["last_checked_at"] = timestamp
        data["last_maintenance_at"] = timestamp
        data["last_maintenance_note"] = note
        append_history(data, "maintenance", note)
        changed = True

    if changed:
        save_log(data)

    status = build_status(data)
    if not args.quiet:
        print_status(status)

    return 10 if status["overdue"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
