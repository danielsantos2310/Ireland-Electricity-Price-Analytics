# Data sources

## SEAI — business electricity and gas prices
- Energy price trends: https://www.seai.ie/data-and-insights/seai-statistics/prices
- Energy prices hub: https://www.seai.ie/data-and-insights/seai-statistics/energy-prices
- EPR Electricity & Gas Prices semester report: https://www.seai.ie/sites/default/files/publications/EPR-Electricity-Gas-Prices.pdf

Used for the main biannual Irish business price target, gas comparison, 2025 S2 consumption-band prices and market shares.

## Eurostat — non-household price components
- Dataset `nrg_pc_205_c`: https://ec.europa.eu/eurostat/databrowser/view/NRG_PC_205_C/default/table?lang=en

Used to decompose Energy & Supply, Network Costs, VAT and taxes/levies by non-household consumption band.

## SEMOpx — Single Electricity Market
- Market data: https://www.semopx.com/market-data/market-results
- Historical-market data guide: https://www.semopx.com/market-data/static-reports/semopx-historical-market-data-final-v2.pdf

Used for Day-Ahead Market price benchmarks and historical look-back validation. Large source workbooks are downloaded by the notebook rather than stored in Git.

## CSO — Wholesale Price Index
- WPM37 dataset API: https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/WPM37/CSV/1.0/en
- Methodology: https://www.cso.ie/en/methods/prices/wholesalepriceindex/introductionofupdatedppiwpiseriesbaseyear2021100/chapter3examplesofchangestoseries/

Used as the monthly wholesale-electricity signal. CSO documents that from January 2019 the electricity index uses the Day-Ahead Single Market Price.

## CRU — network costs and system context
- Commission for Regulation of Utilities: https://www.cru.ie/

Used for qualitative interpretation of network investment, tariffs and retail-price drivers.