# Market Data Sources and Evidence Policy

**Default: free/public access.** Availability, regional access, licensing, rate limits and API terms change. Verify before relying on a provider; do not assume a free tier.

## Cross-market
| Need | Starting sources | Caveats |
|---|---|---|
| Charts / screening | TradingView, Finviz, exchange sites | Free features vary; data may be delayed. |
| Macro series | FRED, ECB Data Portal, national statistical agencies | Prefer primary releases; record observation period. |
| Calendar | Central-bank and exchange calendars; Forex Factory / Investing | Confirm important events with issuer. |
| Filings / news | SEC EDGAR, issuer IR, regulator/exchange notices | Primary documents outrank summaries. |
| Attention | Google Trends, Reddit, X, GitHub Trending | Attention is not demand; watch manipulation. |

## Crypto
CoinGecko or exchange public endpoints for price/market data; DefiLlama for TVL/fees; DEX Screener for pair activity/liquidity; CoinGlass for derivatives context; project docs, governance, GitHub and explorers for primary evidence. Check venue coverage, definitions, timestamps and wash-trading risk. Exchange APIs are venue-specific, not whole-market proxies.

## Equities / ETFs / indices
SEC EDGAR, issuer investor-relations pages, exchange notices and official index/ETF issuer pages. Finviz and TradingView can support screening, but verify material facts in filings. Insider aggregators are leads only; confirm in regulatory filings.

## Commodities / metals
EIA for US energy data, USDA for agriculture, CFTC COT for delayed futures positioning, exchange notices/specifications for contract data, and ETF issuer reports for fund flows. Identify spot, physical, ETF or futures exposure precisely.

## FX
Central-bank statements and official data releases for macro drivers. Public price feeds/charting for technical context. Spot FX is fragmented and generally has no consolidated volume; tick volume is a feed activity proxy, not centralized traded volume.

## Source quality
- A — Primary: regulator, exchange, central bank, issuer filing, official statistical agency, protocol contract/governance source.
- B — Established secondary: reputable vendor or financial publication with transparent methodology.
- C — Discovery only: social posts, anonymous accounts, unverified dashboards or scraped aggregations.

Store provider, exact URL, retrieval timestamp (UTC), period represented, units, publication timestamp, delay/estimate status and quality grade. Every material catalyst needs at least one A/B source. Social posts generate leads, not validation.

## API checklist
Document authentication, free-tier status, request limits, historical depth, update frequency, symbol coverage, timezone, licensing and failure behavior before connecting an API. Cache responsibly. Never commit keys, cookies or personal tokens; use environment variables and exclude local .env files from version control.

## Integrity rules
Never merge prices across currencies without recording FX conversion and timestamp. Preserve raw values and units. Flag missing, stale, outlier or conflicting observations. Do not infer spot volume from futures volume or vice versa.
