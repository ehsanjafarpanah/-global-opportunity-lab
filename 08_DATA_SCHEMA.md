# Candidate Data Schema

This file defines the minimum structured record for every discovered opportunity. The CSV template is in data/candidates_template.csv.

## Required identity and point-in-time fields
- candidate_id: stable unique ID, e.g. EQ-US-NVDA-20261125-01.
- discovered_at_utc: ISO 8601 UTC timestamp.
- market: crypto, equities, commodities, forex, etfs-indices.
- instrument, venue, quote_currency, discovery_price.
- timeframe and benchmark where relevant.

## Evidence
Each material claim should have a URL, source grade (A/B/C), publication timestamp and retrieval timestamp. The starter CSV has three evidence slots; add more evidence in the notes or a linked evidence file when necessary. A candidate without verifiable evidence remains Discovery or is rejected.

## Ratings and score
Use 0–5 ratings for the dimensions defined in 03_SCORING_MODEL.md. Calculate weighted points using the agreed weights. Do not confuse the six abbreviated rating columns in the CSV with a full scoring breakdown: record dimension-level rationale in the daily log. If a dimension is N/A, explain the market-specific treatment; do not enter zero by default.

## Status values
Discovery, Watchlist, Research Priority, Entry Candidate, Active, Paused, Rejected, Closed.

## Data rules
- Preserve original discovery-time values. Append updates; do not rewrite history.
- Use decimal dot for numeric values and ISO dates/timestamps.
- Do not mix instruments or venues under one record.
- Keep secrets and account-specific data out of public records.
- Do not treat a discovery-price return as an executable trade return.
