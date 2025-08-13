# visualization.py
import matplotlib.pyplot as plt
import pandas as pd

def plot_single_factor(X_train: pd.DataFrame, y_train, feature: str, color="goldenrod"):
    plt.scatter(X_train[feature], y_train, color=color)
    plt.xlabel(feature.capitalize())
    plt.ylabel("MPG")
    plt.title(f"{feature.capitalize()} to MPG (Training Dataset)")
    plt.show()

def plot_regression_comparison(
    X_train: pd.DataFrame,
    y_train,
    models_info,
    x_feature="displacement"
):
    """
    models_info: list of tuples (label, model, featurizer).
    For comparison, as in your code, we draw ŷ on X_train[x_feature].
    """
    plt.scatter(X_train[x_feature], y_train, label="Experimental data", color="lightcoral")
    for label, model, featurizer in models_info:
        Xd = featurizer(X_train)
        yhat = model.predict(Xd)
        plt.plot(X_train[x_feature], yhat, label=label)
    plt.xlabel("Displacement")
    plt.ylabel("MPG")
    plt.title("Comparison of regression models")
    plt.legend()
    plt.show()

def plot_optimal_fit(X_train: pd.DataFrame, y_train, model, featurizer, label):
    plt.scatter(X_train["displacement"], y_train, label="Experimental data", color="lightcoral")
    yhat = model.predict(featurizer(X_train))
    plt.plot(X_train["displacement"], yhat, label=label, color="seagreen")
    plt.xlabel("Displacement")
    plt.ylabel("MPG")
    plt.title("Optimal model")
    plt.legend()
    plt.show()
