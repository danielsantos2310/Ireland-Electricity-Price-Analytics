# Ireland Electricity Price Analytics

An independent, reproducible analysis of Irish business electricity prices, the 2021–2023 energy shock, customer-size differences, wholesale-market signals and transparent 2026–2035 price scenarios.


## Explore

- **Interactive story:** https://danielsantos2310.github.io/Ireland-Electricity-Price-Analytics/
- **Open final notebook in Colab:** https://colab.research.google.com/github/danielsantos2310/Ireland-Electricity-Price-Analytics/blob/1c418ba5849dfbb8c10f81eaea18adaac21c1348/notebooks/Ireland_Electricity_Price_Analytics_Final.ipynb

## Research question

**Why did Irish business electricity prices change so sharply, who paid what, and what range of prices is plausible under different 2035 system-cost assumptions?**

## Highlights

- Weighted-average business electricity: **13.79 c/kWh (2015) → 23.49 c/kWh (2025)**.
- Semester peak: **28.40 c/kWh in 2022 S2**.
- Large-user Band IG: **15.9 c/kWh in 2025 S2**, versus **22.7 c/kWh** weighted average.
- Walk-forward validation: a simple **last-price naive forecast** beat Holt, linear-trend and gas-augmented alternatives over the broader 2018–2025 test window.
- 2035 weighted-average business scenarios in real 2025 money: **21.2 / 24.4 / 30.1 c/kWh** (low / central / high).

## Project structure

```text
.
├── index.html
├── assets/
├── data/
│   ├── raw/
│   ├── processed/
│   └── site_data.json
├── docs/
├── notebooks/
│   └── Ireland_Electricity_Price_Analytics_Final.ipynb
└── src/
```

## Tech & topics

`Python` · `pandas` · `time-series` · `forecasting` · `data-analysis` · `data-visualization` · `energy` · `Ireland` · `electricity-prices`

## Sources

Primary evidence comes from **SEAI**, **Eurostat**, **SEMOpx**, **CSO** and **CRU**. See `docs/data_sources.md`.

## Important interpretation

The 2035 outputs are analytical scenarios, **not official forecasts or statistical confidence intervals**. Band IG is a public large-user consumption band, not a data-centre tariff.

## Deployment

**Pages status:** enabled. The interactive story is deployed from `main` through GitHub Actions and GitHub Pages.

## Reproduce

Open the final notebook in Jupyter or Colab and run top-to-bottom. Some source cells download official public datasets directly; large SEMOpx look-back workbooks are not committed to the repository.