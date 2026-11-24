# Tools and Automation Roadmap

## Phase 0 — Manual validation
Use the daily checklist and CSV schema. Confirm that the method produces consistent, auditable candidate records before coding data ingestion.

## Phase 1 — Local data hygiene (Python standard library)
Run the candidate-register validator from the repository root:

```bash
python tools/validate_candidates.py data/candidates_template.csv
python tools/validate_candidates.py path/to/candidates.csv --strict
```

It checks the canonical CSV schema, timezone-aware discovery timestamps, duplicate IDs, market/status labels, 3–30 day horizon, positive discovery price, seven rating fields (0–5), weighted score arithmetic, and required entry/invalidation fields. `--strict` also fails on warnings. It does not fetch prices, verify evidence claims, or generate signals.

## Phase 2 — Free/public data connectors
Add one connector at a time, starting with reliable public endpoints and documented terms. Each connector must record retrieval time, source timestamp, units, coverage and failure state. Do not scrape sites in ways that violate terms or bypass access controls.

## Phase 3 — Screening and reporting
Normalize data by market, calculate technical/relative-strength features, rank candidates and generate dated Markdown/CSV reports. Keep raw inputs separate from derived metrics.

## Phase 4 — Evaluation
Automate scheduled outcome snapshots and calculate forward metrics. Preserve historical snapshots to prevent look-ahead bias.

## Engineering rules
- Python standard library first; add dependencies only when they provide a clear benefit.
- Keep API credentials in environment variables or a local ignored .env file.
- Never commit secrets, session cookies or personal account data.
- Log errors and stale data; do not silently substitute missing values.
- Every connector must be independently testable and safe to disable.
