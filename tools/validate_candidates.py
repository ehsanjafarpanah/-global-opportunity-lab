#!/usr/bin/env python3
"""Validate candidate-register CSV rows for Global Opportunity Lab.

Standard-library only. This checks schema, required identifiers, dates, scores,
evidence freshness, and basic risk/entry fields. It does NOT fetch prices,
verify claims, generate trading signals, or replace human review.

Usage:
  python tools/validate_candidates.py data/candidates_template.csv
  python tools/validate_candidates.py path/to/candidates.csv --strict
"""
from __future__ import annotations

import argparse
import csv
import sys
from datetime import date, datetime, timezone
from pathlib import Path

REQUIRED_COLUMNS = {
    "candidate_id", "discovery_date", "market", "symbol", "instrument",
    "direction", "discovery_price", "currency", "timeframe_days",
    "catalyst", "technical_evidence", "flow_evidence",
    "fundamental_evidence", "sentiment_evidence", "macro_fit",
    "invalidation", "entry_confirmation", "status",
}
SCORE_COLUMNS = {
    "catalyst_score": 20,
    "technical_score": 20,
    "flows_score": 15,
    "fundamental_score": 15,
    "sentiment_score": 10,
    "macro_score": 10,
    "risk_score": 10,
}
VALID_MARKETS = {"crypto", "equities", "commodities", "forex", "etfs-indices"}
VALID_DIRECTIONS = {"long", "short", "both", "watch"}
VALID_STATUSES = {
    "discovery", "watchlist", "research_priority", "entry_candidate",
    "active", "paused", "rejected", "closed",
}


def parse_date(value: str) -> date | None:
    if not value.strip():
        return None
    try:
        return date.fromisoformat(value.strip())
    except ValueError:
        return None


def number(value: str) -> float | None:
    if not value.strip():
        return None
    try:
        return float(value.replace(",", "").strip())
    except ValueError:
        return None


def validate(path: Path, strict: bool) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            headers = set(reader.fieldnames or [])
            missing = sorted(REQUIRED_COLUMNS - headers)
            if missing:
                errors.append("Missing required columns: " + ", ".join(missing))
                print_report(errors, warnings)
                return 1

            rows = list(reader)
    except OSError as exc:
        print(f"ERROR: cannot read {path}: {exc}", file=sys.stderr)
        return 2

    seen: set[str] = set()
    today = datetime.now(timezone.utc).date()

    for line, row in enumerate(rows, start=2):
        prefix = f"row {line}"
        cid = (row.get("candidate_id") or "").strip()
        symbol = (row.get("symbol") or "").strip()
        market = (row.get("market") or "").strip().lower()
        direction = (row.get("direction") or "").strip().lower()
        status = (row.get("status") or "").strip().lower()

        if not cid:
            errors.append(f"{prefix}: candidate_id is blank")
        elif cid in seen:
            errors.append(f"{prefix}: duplicate candidate_id {cid!r}")
        seen.add(cid)

        if not symbol:
            errors.append(f"{prefix}: symbol is blank")
        if market and market not in VALID_MARKETS:
            errors.append(f"{prefix}: unsupported market {market!r}")
        if direction and direction not in VALID_DIRECTIONS:
            errors.append(f"{prefix}: direction must be one of {sorted(VALID_DIRECTIONS)}")
        if status and status not in VALID_STATUSES:
            errors.append(f"{prefix}: unsupported status {status!r}")

        discovered = parse_date(row.get("discovery_date") or "")
        if discovered is None:
            errors.append(f"{prefix}: discovery_date must be YYYY-MM-DD")
        elif discovered > today:
            errors.append(f"{prefix}: discovery_date is in the future")

        price = number(row.get("discovery_price") or "")
        if price is None or price <= 0:
            errors.append(f"{prefix}: discovery_price must be a positive number")

        horizon = number(row.get("timeframe_days") or "")
        if horizon is None or not 3 <= horizon <= 30:
            errors.append(f"{prefix}: timeframe_days must be between 3 and 30")

        total = 0.0
        score_complete = True
        for field, weight in SCORE_COLUMNS.items():
            raw = row.get(field)
            if raw is None or not raw.strip():
                score_complete = False
                continue
            value = number(raw)
            if value is None or not 0 <= value <= 5:
                errors.append(f"{prefix}: {field} must be between 0 and 5")
            else:
                total += value * weight / 5

        if score_complete:
            if "score_total" in row and (row.get("score_total") or "").strip():
                stored = number(row["score_total"])
                if stored is None or abs(stored - total) > 0.11:
                    errors.append(
                        f"{prefix}: score_total mismatch; calculated {total:.1f}, "
                        f"stored {row['score_total']!r}"
                    )
        else:
            warnings.append(f"{prefix}: incomplete score; do not rank as fully scored")

        for field in ("catalyst", "technical_evidence", "invalidation",
                      "entry_confirmation"):
            if not (row.get(field) or "").strip():
                warnings.append(f"{prefix}: {field} is blank")

        if status == "entry_candidate":
            for field in ("invalidation", "entry_confirmation",
                          "technical_evidence", "discovery_price"):
                if not (row.get(field) or "").strip():
                    errors.append(
                        f"{prefix}: entry_candidate requires {field}"
                    )

        if status == "active" and not (row.get("invalidation") or "").strip():
            errors.append(f"{prefix}: active candidate requires invalidation")

    print(f"Validated {len(rows)} candidate row(s) from {path}")
    print_report(errors, warnings)
    if strict and warnings:
        return 1
    return 1 if errors else 0


def print_report(errors: list[str], warnings: list[str]) -> None:
    for item in errors:
        print("ERROR:", item)
    for item in warnings:
        print("WARNING:", item)
    print(f"Summary: {len(errors)} error(s), {len(warnings)} warning(s)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument(
        "--strict", action="store_true",
        help="return non-zero when warnings are present",
    )
    args = parser.parse_args()
    return validate(args.csv_file, args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
