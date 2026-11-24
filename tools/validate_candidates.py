#!/usr/bin/env python3
"""Validate Global Opportunity Lab candidate CSV records (Python stdlib only).

Usage:
  python tools/validate_candidates.py data/candidates_template.csv
  python tools/validate_candidates.py path/to/candidates.csv --strict

This validates record hygiene and score arithmetic. It does not fetch or verify
market data, validate evidence truth, calculate trade signals, or give advice.
"""
from __future__ import annotations
import argparse
import csv
import sys
from datetime import date, datetime, timezone
from pathlib import Path

REQUIRED = {
    "candidate_id", "discovered_at_utc", "market", "instrument", "venue",
    "quote_currency", "discovery_price", "timeframe", "signal_family",
    "thesis", "catalyst", "catalyst_rating", "evidence_url_1",
    "technical_rating", "flow_rating", "fundamental_rating",
    "sentiment_rating", "macro_rating", "risk_rating", "total_score",
    "confidence", "status", "entry_condition", "invalidation",
}
WEIGHTS = {
    "catalyst_rating": 20, "technical_rating": 20, "flow_rating": 15,
    "fundamental_rating": 15, "sentiment_rating": 10,
    "macro_rating": 10, "risk_rating": 10,
}
MARKETS = {"crypto", "equities", "commodities", "forex", "etfs-indices"}
STATUSES = {
    "discovery", "watchlist", "research priority", "research_priority",
    "entry candidate", "entry_candidate", "active", "paused", "rejected", "closed",
}
CONFIDENCE = {"low", "medium", "high", "unverified", "preliminary"}

def num(value: str):
    try:
        return float(value.replace(",", "").strip())
    except (ValueError, AttributeError):
        return None

def parse_timestamp(value: str):
    if not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            return None
        return parsed
    except ValueError:
        return None

def validate(path: Path, strict: bool) -> int:
    errors, warnings = [], []
    try:
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            headers = set(reader.fieldnames or [])
            missing = sorted(REQUIRED - headers)
            if missing:
                print("ERROR: missing columns: " + ", ".join(missing))
                return 1
            rows = list(reader)
    except OSError as exc:
        print(f"ERROR: cannot read {path}: {exc}", file=sys.stderr)
        return 2

    seen = set()
    now = datetime.now(timezone.utc)
    for line, row in enumerate(rows, 2):
        p = f"row {line}"
        cid = (row.get("candidate_id") or "").strip()
        if not cid:
            errors.append(f"{p}: candidate_id is blank")
        elif cid in seen:
            errors.append(f"{p}: duplicate candidate_id {cid!r}")
        seen.add(cid)

        market = (row.get("market") or "").strip().lower()
        if market not in MARKETS:
            errors.append(f"{p}: unsupported or blank market {market!r}")
        if not (row.get("instrument") or "").strip():
            errors.append(f"{p}: instrument is blank")
        if not (row.get("venue") or "").strip():
            warnings.append(f"{p}: venue is blank; instrument may be ambiguous")
        ts = parse_timestamp(row.get("discovered_at_utc") or "")
        if ts is None:
            errors.append(f"{p}: discovered_at_utc must be ISO-8601 with timezone")
        elif ts > now:
            errors.append(f"{p}: discovered_at_utc is in the future")

        price = num(row.get("discovery_price") or "")
        if price is None or price <= 0:
            errors.append(f"{p}: discovery_price must be positive")
        horizon = num(row.get("timeframe") or "")
        if horizon is None or not 3 <= horizon <= 30:
            errors.append(f"{p}: timeframe must be between 3 and 30 days")

        status = (row.get("status") or "").strip().lower()
        if status not in STATUSES:
            errors.append(f"{p}: invalid status {status!r}")
        confidence = (row.get("confidence") or "").strip().lower()
        if confidence and confidence not in CONFIDENCE:
            warnings.append(f"{p}: non-standard confidence label {confidence!r}")

        total = 0.0
        complete = True
        for field, weight in WEIGHTS.items():
            raw = row.get(field) or ""
            value = num(raw)
            if value is None:
                complete = False
                continue
            if not 0 <= value <= 5:
                errors.append(f"{p}: {field} must be between 0 and 5")
            else:
                total += value * weight / 5
        stored = num(row.get("total_score") or "")
        if complete:
            if stored is None or abs(stored - total) > 0.11:
                errors.append(f"{p}: total_score mismatch; calculated {total:.1f}, stored {row.get('total_score')!r}")
        else:
            warnings.append(f"{p}: incomplete ratings; total score cannot be recomputed")

        for field in ("thesis", "catalyst", "entry_condition", "invalidation"):
            if not (row.get(field) or "").strip():
                warnings.append(f"{p}: {field} is blank")
        if status in {"entry candidate", "entry_candidate", "active"}:
            for field in ("entry_condition", "invalidation", "evidence_url_1"):
                if not (row.get(field) or "").strip():
                    errors.append(f"{p}: {status} requires {field}")

    for item in errors:
        print("ERROR:", item)
    for item in warnings:
        print("WARNING:", item)
    print(f"Validated {len(rows)} row(s): {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors or (strict and warnings) else 0

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    return validate(args.csv_file, args.strict)

if __name__ == "__main__":
    raise SystemExit(main())
