"""Small helpers used by the Ireland Electricity Price Analytics notebook."""
from __future__ import annotations

import numpy as np
import pandas as pd

def add_period_fields(df: pd.DataFrame, period_col: str = "period") -> pd.DataFrame:
    out = df.copy()
    out["year"] = out[period_col].str[:4].astype(int)
    out["semester"] = out[period_col].str[-1].astype(int)
    return out

def semester_from_month(month: int) -> int:
    return 1 if int(month) <= 6 else 2

def mape(y_true, y_pred) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    mask = y_true != 0
    return float(np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100)