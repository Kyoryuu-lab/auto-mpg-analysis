# results_calculator.py
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

def evaluate_model(model, featurizer, X, y):
    """Calculates metrics for a model."""
    y_pred = model.predict(featurizer(X))
    return {
        "R2": r2_score(y, y_pred),
        "MSE": mean_squared_error(y, y_pred),
        "MAE": mean_absolute_error(y, y_pred)
    }

def compare_models(models_info, X_test, y_test):
    """
    models_info — list of tuples: (model_name, model, featurizer)
    Returns a dictionary {name: {R2, MSE, MAE}}
    """
    results = {}
    for name, model, featurizer in models_info:
        results[name] = evaluate_model(model, featurizer, X_test, y_test)
    return results

