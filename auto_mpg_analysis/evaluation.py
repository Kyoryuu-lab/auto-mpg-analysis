# evaluation.py
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import pandas as pd

def evaluate(model, X_design, y_true):
    y_pred = model.predict(X_design)
    return {
        "R2": r2_score(y_true, y_pred),
        "MSE": mean_squared_error(y_true, y_pred),
        "MAE": mean_absolute_error(y_true, y_pred),
    }

def print_split_means(X_train: pd.DataFrame, X_test: pd.DataFrame, cols):
    for c in cols:
        print(f"The average value of {c} in the training sample: {X_train[c].mean():.3f}")
        print(f"The average value of {c} in the test sample:    {X_test[c].mean():.3f}")
