# models.py
import statsmodels.api as sm
from typing import Callable, Dict, Tuple
import pandas as pd
from features import build_poly_features

def _with_const(df: pd.DataFrame) -> pd.DataFrame:
    return sm.add_constant(df, has_constant="add")

def make_linear_featurizer(cols) -> Callable[[pd.DataFrame], pd.DataFrame]:
    def f(X: pd.DataFrame) -> pd.DataFrame:
        return _with_const(X[list(cols)])
    return f

def make_poly_featurizer(cols, interactions=False) -> Callable[[pd.DataFrame], pd.DataFrame]:
    def f(X: pd.DataFrame) -> pd.DataFrame:
        feats = build_poly_features(X, base_cols=cols, degree=2, interactions=interactions)
        return _with_const(feats)
    return f

def train_ols(X_design: pd.DataFrame, y) -> sm.regression.linear_model.RegressionResultsWrapper:
    return sm.OLS(y, X_design).fit()

def train_linear(X_train: pd.DataFrame, y_train, cols):
    """Linear Regression: returns (model, featurizer, used_cols)."""
    featurizer = make_linear_featurizer(cols)
    Xtr = featurizer(X_train)
    model = train_ols(Xtr, y_train)
    return model, featurizer, list(cols)

def train_poly2(X_train: pd.DataFrame, y_train, cols, interactions=False):
    """2nd order polynomial (with/without interactions): returns (model, featurizer, used_cols)."""
    featurizer = make_poly_featurizer(cols, interactions=interactions)
    Xtr = featurizer(X_train)
    model = train_ols(Xtr, y_train)
    return model, featurizer, list(cols)
