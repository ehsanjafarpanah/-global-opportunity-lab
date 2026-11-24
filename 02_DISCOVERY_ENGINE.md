# Discovery Engine Specification

## Four signal families
1. Price / relative strength: trend change, range compression, breakout/retest, relative strength vs benchmark and unusual volatility.
2. Fundamental / event acceleration: earnings revisions, filings, product or regulatory catalysts, protocol usage/fees, macro releases and supply/inventory shocks.
3. Capital flows / positioning: ETF flows, exchange flows, relevant volume, open interest, COT positioning and sector rotation.
4. Narrative / attention: rising search/social/developer attention, independently confirmed and ideally translating into usage, flows or price behavior.

## Screening sequence
1. Define eligible universe and minimum liquidity per market.
2. Capture regime and event calendar.
3. Run technical and relative-strength screens.
4. Add verifiable catalysts and flow anomalies.
5. Treat social attention as a lead, not proof.
6. Deduplicate instruments and correlated exposures.
7. Apply hard exclusions before scoring.
8. Retain up to 15 candidates; deep-research at most three.

## Candidate evidence card
ID; discovered_at_utc; market; instrument; venue; quote currency; discovery price; benchmark/timeframe; signal family; thesis; catalyst/window; evidence URLs with grade and published/retrieved timestamps; technical state/levels; liquidity/spread; bull/base/bear cases; entry trigger; invalidation; targets; estimated R/R; score; confidence; status; counter-evidence.

## Confidence
- High: multiple independent A/B sources, fresh data, clear setup and no material unresolved contradiction.
- Medium: credible evidence but incomplete confirmation or meaningful uncertainty.
- Low: mostly C-grade sources, stale/conflicting data or unclear catalyst/setup.

Confidence is not score. High score with low confidence is not actionable.

## Early signal archetypes
Accumulation before confirmed breakout; fundamental acceleration before consensus repricing; narrative formation with measurable adoption/flows; event-driven dislocation with defined risk; relative-strength rotation.

## Rejection reasons
Record explicit reasons: insufficient liquidity, stale data, unverified catalyst, excessive event/gap risk, poor R/R, extended price, conflicting evidence, crowded positioning or invalidated thesis.
