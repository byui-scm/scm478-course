"""
Unit 1 self-checks for SCM 478.
Verifies that the Week 1 data files are present and readable.

This module is loaded by setup/self_check.py, which sets REPO_ROOT
before calling run_checks().
"""

from pathlib import Path

# REPO_ROOT is injected by self_check.py at load time
REPO_ROOT = Path(__file__).parent.parent.parent


REQUIRED_FILES = [
    "Products___Pricing.csv",
    "Ingredient_Catalog.csv",
]

EXPECTED_COLUMNS = {
    "Products___Pricing.csv": [
        "SKU", "Product Name", "Description", "Category",
        "Unit of Measure", "Retail Price",
    ],
    "Ingredient_Catalog.csv": [
        "Ingredient SKU", "Description", "Order Unit", "Cost Per Unit",
        "MOQ", "Primary Supplier ID", "Primary Supplier Name",
    ],
}


def run_checks():
    """Return a list of error strings. Empty list means all passed."""
    errors = []
    data_dir = REPO_ROOT / "data"

    if not data_dir.is_dir():
        errors.append("data/ folder not found — cannot run file checks")
        return errors

    try:
        import pandas as pd
    except ImportError:
        errors.append("pandas not installed — cannot read CSV files")
        return errors

    for filename in REQUIRED_FILES:
        filepath = data_dir / filename
        if not filepath.exists():
            errors.append(f"{filename} not found in data/")
            continue

        try:
            df = pd.read_csv(filepath)
        except Exception as e:
            errors.append(f"{filename} could not be read: {e}")
            continue

        if len(df) == 0:
            errors.append(f"{filename} is empty")
            continue

        expected_cols = EXPECTED_COLUMNS.get(filename, [])
        missing_cols = [c for c in expected_cols if c not in df.columns]
        if missing_cols:
            errors.append(
                f"{filename} missing columns: {', '.join(missing_cols)}"
            )

    return errors
