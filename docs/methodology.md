# Methodology

## 1. Price target
The main target is the **SEAI biannual weighted-average non-household electricity price, ex VAT**. The commercial quarterly comparison is not treated as an independent quarterly target because adjacent values frequently repeat.

## 2. Historical analysis
The public story focuses on 2015–2025, while modelling uses the longer 2008–2025 history where comparable data are available.

## 3. Wholesale layer
SEMOpx Day-Ahead Market data and CSO WPM37 are used as explanatory wholesale signals. Over the overlapping period, their normalised movements are nearly identical.

## 4. Forecast-model validation
Candidate models are evaluated with **rolling-origin / walk-forward validation**. No random train/test split is used. Metrics include MAE, RMSE, MAPE and R².

A simple persistence forecast (`next period = last observed price`) is retained as the benchmark. More complex models are accepted only if they improve out-of-sample performance.

## 5. 2035 scenario engine
Because long-run retail prices depend on future wholesale energy, networks, levies, policy and inflation, the project does not publish one deterministic 2035 point forecast.

The 2025 observed price is decomposed into:
- Energy & Supply
- Network Costs
- Taxes / levies / other components

Three transparent annual-growth assumption sets are applied:
- Low-cost transition
- Central
- High-cost / constrained

Both **real 2025-money** and **nominal** paths are shown.

## 6. Large-user analysis
Band IG (`>150,000 MWh/year`) is presented as the closest public large-user benchmark. It is **not** assumed to equal a data-centre tariff or any specific negotiated contract.

## 7. Limitations
- Scenarios are not official forecasts or statistical confidence intervals.
- Retail-minus-wholesale is not interpreted as supplier margin.
- Structural breaks such as the 2021–2023 energy crisis make long-horizon extrapolation uncertain.
- Network tariffs and tax treatment vary by customer and can change with regulation.