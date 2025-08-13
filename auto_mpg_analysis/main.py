# main.py
from data_loader import load_data, train_test_split_xy
from models import train_linear, train_poly2, make_linear_featurizer
from evaluation import print_split_means
from visualization import (
    plot_single_factor,
    plot_regression_comparison,
    plot_optimal_fit,
)
from results_calculator import compare_models
from results_saver import save_results_to_desktop

def main():
    # === Download and split ===
    data = load_data()
    X_train, X_test, y_train, y_test = train_test_split_xy(
        data, feature_cols=("displacement", "horsepower")
    )

    # Representativeness check
    print_split_means(X_train, X_test, cols=("displacement", "horsepower"))

    # === Visualization ===
    plot_single_factor(X_train, y_train, "displacement")
    plot_single_factor(X_train, y_train, "horsepower")

    # === Models ===
    model_lm, feat_lm, _ = train_linear(X_train, y_train, cols=("displacement", "horsepower"))
    model_poly, feat_poly, _ = train_poly2(X_train, y_train, cols=("displacement", "horsepower"), interactions=False)
    model_poly_int, feat_poly_int, _ = train_poly2(X_train, y_train, cols=("displacement", "horsepower"), interactions=True)

    # === Comparison graphs ===
    plot_regression_comparison(
        X_train, y_train,
        models_info=[
            ("Linear regression", model_lm, feat_lm),
            ("Polynomial (2nd order)", model_poly, feat_poly),
            ("Polynomial (with interaction)", model_poly_int, feat_poly_int),
        ],
        x_feature="displacement"
    )

    # === Metrics and saving results ===
    results = compare_models(
        [
            ("Linear regression", model_lm, feat_lm),
            ("Polynomial (2nd order)", model_poly, feat_poly),
            ("Polynomial (with interaction)", model_poly_int, feat_poly_int),
        ],
        X_test, y_test
    )

    save_results_to_desktop(results)

    # === Optimal model (graph) ===
    plot_optimal_fit(
        X_train, y_train,
        model=model_poly_int, featurizer=feat_poly_int,
        label="Polynomial regression with interaction terms"
    )

if __name__ == "__main__":
    main()
