# features.py
import pandas as pd
import itertools

def add_squared_features(X: pd.DataFrame, cols=None) -> pd.DataFrame:
    X2 = X.copy()
    cols = cols or list(X.columns)
    for c in cols:
        X2[f"{c}_squared"] = X2[c] ** 2
    return X2

def add_pairwise_interactions(X: pd.DataFrame, cols=None) -> pd.DataFrame:
    X2 = X.copy()
    cols = cols or list(X.columns)
    for a, b in itertools.combinations(cols, 2):
        X2[f"{a}_{b}"] = X2[a] * X2[b]
    return X2

def build_poly_features(
    X: pd.DataFrame,
    base_cols,
    degree: int = 2,
    interactions: bool = False
) -> pd.DataFrame:
    """Builds polynomial features up to 2nd order with the option of interactions."""
    Xb = X[list(base_cols)].copy()
    if degree >= 2:
        Xb = add_squared_features(Xb, cols=base_cols)
    if interactions:
        Xb = add_pairwise_interactions(Xb, cols=base_cols)
    return Xb
