# data_loader.py
import pandas as pd
from sklearn.model_selection import train_test_split

AUTO_MPG_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
)
AUTO_MPG_COLUMNS = [
    "mpg", "cylinders", "displacement", "horsepower", "weight",
    "acceleration", "model year", "origin", "car name"
]

def load_data(url: str = AUTO_MPG_URL) -> pd.DataFrame:
    """Loads and clears Auto MPG."""
    df = pd.read_csv(url, delim_whitespace=True, names=AUTO_MPG_COLUMNS, na_values="?")
    df = df.dropna().reset_index(drop=True)
    return df

def train_test_split_xy(
    df: pd.DataFrame,
    feature_cols=("displacement", "horsepower"),
    target_col="mpg",
    test_size=0.3,
    random_state=42
):
    """Splits into training/test samples."""
    X = df[list(feature_cols)].copy()
    y = df[target_col].copy()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test
