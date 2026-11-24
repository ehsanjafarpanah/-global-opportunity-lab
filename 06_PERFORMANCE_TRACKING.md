# Performance Tracking and Method Validation

## Preserve point-in-time records
At discovery, store timestamp, price, source URLs, score, confidence, thesis and planned levels. Never overwrite the original snapshot; append updates. Use UTC internally and retain source/local timestamps.

## Outcome checkpoints
Review at 1D, 3D, 7D, 14D and 30D: reference price and return from discovery; maximum favorable excursion (MFE); maximum adverse excursion (MAE); whether entry condition occurred; whether invalidation preceded target; catalyst/thesis outcome; data availability and confidence changes.

For shorts, define return and excursion direction consistently. State whether returns include fees, funding, borrow, slippage and FX conversion.

## Core metrics
Precision; false-positive rate; hit rate by market/setup/score/confidence; average and median forward return; MFE/MAE; realized R multiples for executable entries; time-to-trigger and time-to-invalidation; source freshness, coverage, contradiction and failure rates.

Discovery-price returns are not necessarily executable trade returns and must not be presented as strategy profitability.

## Bias controls
Avoid look-ahead and survivorship bias; retain delisted/failed candidates where possible. Do not rewrite theses retrospectively. Compare with relevant benchmarks and a no-signal baseline. Separate in-sample tuning from out-of-sample evaluation. Publish sample size and uncertainty before changing weights.

## Weekly review
Review due candidates; classify wins/losses/missed triggers/false positives; identify weak sources and failure modes; compare by market/setup; propose one controlled change at a time; record it in 07_DECISIONS_LOG.md.
