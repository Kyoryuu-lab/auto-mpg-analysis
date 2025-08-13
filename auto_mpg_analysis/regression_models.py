# regression_models.py
import statsmodels.api as sm

def train_linear_regression(X_train, y_train):
    X_train_lm = sm.add_constant(X_train)
    model = sm.OLS(y_train, X_train_lm).fit()
    return model

def train_polynomial_regression(X_train, y_train, interaction=False):
    X_poly = X_train.copy()
    for col in X_train.columns:
        X_poly[f"{col}_squared"] = X_poly[col] ** 2
    if interaction:
        cols = list(X_train.columns)
        for i in range(len(cols)):
            for j in range(i+1, len(cols)):
                X_poly[f"{cols[i]}_{cols[j]}"] = X_poly[cols[i]] * X_poly[cols[j]]
    X_poly_lm = sm.add_constant(X_poly)
    model = sm.OLS(y_train, X_poly_lm).fit()
    return model
