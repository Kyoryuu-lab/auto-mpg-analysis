# results_saver.py
import os
from datetime import datetime

def save_results_to_desktop(results_dict, filename="auto_mpg_results.txt"):
    """
    Saves results in TXT on the desktop, appending to the end.
    results_dict — dictionary of the form:
    {
    "Model1": {"R2": ..., "MSE": ..., "MAE": ...},
    "Model2": {...}
    }
    """
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    results_file = os.path.join(desktop_path, filename)

    with open(results_file, "a", encoding="utf-8") as f:
        f.write(f"=== Test from {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        f.write("Model | R² | MSE | MAE\n")
        f.write("----------------------------\n")
        for model_name, metrics in results_dict.items():
            f.write(
                f"{model_name} | {metrics['R2']:.3f} | "
                f"{metrics['MSE']:.3f} | {metrics['MAE']:.3f}\n"
            )
        f.write("\n")  # empty line between tests

    print(f"[INFO] Results added to {results_file}")

