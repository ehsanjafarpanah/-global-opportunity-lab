# Global Opportunity Lab — Master Method

**Status:** v1.0 baseline  
**Mandate:** discover and validate short-horizon (3–30 day) opportunities across crypto, equities, commodities, FX, ETFs and indices.  
**Constraints:** free/public sources first; medium risk tolerance; wait-for-confirmation entries; combined fundamental, technical, flow and sentiment analysis.

## Principles
1. Evidence before narrative. Every material claim needs a source, timestamp and confidence label.
2. Discovery is not a trade signal. A high score never overrides a failed risk gate.
3. Do not chase extended price. Prefer a defined setup, invalidation and favorable payoff.
4. Compare like with like: spot vs spot, futures vs futures, same venue and timeframe where possible.
5. Mark unavailable data as N/A; never silently treat it as zero.
6. Record discovery-time price and evidence to prevent look-ahead bias.
7. Free access is the default. Verify API limits, licensing and free-tier terms before automation.

## Scope and horizon
Markets: crypto, listed equities, commodities/metals, major FX pairs, ETFs and indices. Primary horizon: 3–30 calendar days. Daily discovery; 1–7 day validation. Longer-term theses belong in a separate research track.

## Five-stage pipeline
### A. Market regime
Record volatility, trend, breadth, rates, USD conditions and scheduled events relevant to each market.

### B. Broad discovery
Screen liquid instruments for relative strength/weakness, unusual activity, catalysts, flow changes and independent attention. Retain up to 15 raw candidates per daily run.

### C. Validation
Seek at least three independent evidence classes: (1) market evidence, (2) verifiable driver/catalyst, and (3) independent confirmation. Multiple sites repeating one press release are not independent.

### D. Deep research
Deep-dive no more than three candidates per daily cycle. Capture instrument, venue, quote currency, timestamp/timezone, discovery price, catalyst/timing, daily and 4-hour structure, levels, ATR/volatility, liquidity/spread, bull/base/bear cases, entry zone, invalidation, targets, reward/risk, event risks, evidence links and confidence.

### E. Decision state
Allowed states: Discovery, Watchlist, Research Priority, Entry Candidate, Active, Paused, Rejected, Closed. Entry Candidate requires explicit confirmation criteria and invalidation.

## Daily operating loop
1. Snapshot regime and calendar.
2. Run market-specific screens; retain up to 15 candidates.
3. Remove illiquid, stale, duplicate or unverified candidates.
4. Validate with three evidence classes.
5. Deep-dive up to three; score and apply hard gates.
6. Publish a dated watchlist, including rejections and reasons.
7. Revisit prior candidates without rewriting original discovery records.

Initial manual workflow target: 30–45 minutes/day; this is a process target, not a promise of coverage or returns.

## Market-specific interpretation
Use the module under markets/. Do not apply crypto metrics to equities or treat futures positioning as spot demand. Mark inapplicable metrics N/A and use a documented market-specific scoring profile.

## Candidate record standard
Every record must include ID, timestamp/timezone, market, instrument, venue, discovery price, thesis, catalyst, evidence links, score, confidence, status, entry condition, invalidation, targets, estimated R/R, event risks and review dates at 1D/3D/7D/14D/30D.

## Evaluation and governance
Evaluate precision, hit rate by setup, false positives, MAE/MFE, risk-adjusted outcomes and source quality. Avoid tuning weights on tiny samples. Record every methodology change in 07_DECISIONS_LOG.md with rationale and review date.

This is a research and decision-support framework, not personalized financial advice, execution software or a guarantee of performance.
