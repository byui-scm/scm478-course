"""
SCM 478 - Unit 1 Checks: Peak Fuel Dashboard (Weeks 1-4)

Each assignment is a separate function that returns a list of
(name, passed, detail, points) tuples.

The get_assignments() function registers which assignments are
available. The instructor controls what students see by adding
or removing entries from that function before releasing the file.
"""

import pandas as pd
import os


# ==================================================================
# HELPERS
# ==================================================================
def _find_file(candidates):
    """Return the first matching filename, or None."""
    for fname in candidates:
        if os.path.exists(fname):
            return fname
    return None


def _read_app_code():
    """Read the main app file and return its contents."""
    for fname in ["app.py", "main.py", "streamlit_app.py"]:
        if os.path.exists(fname):
            with open(fname, "r", encoding="utf-8", errors="replace") as f:
                return f.read()
    return None


def _load_products():
    """Load Products & Pricing. Returns (df, filename) or (None, None)."""
    f = _find_file([
        "Products___Pricing.csv", "Products_Pricing.csv",
        "products_pricing.csv", "Products & Pricing.csv",
    ])
    if f:
        try:
            return pd.read_csv(f), f
        except Exception:
            return None, f
    return None, None


def _load_ingredients():
    """Load Ingredient Catalog. Returns (df, filename) or (None, None)."""
    f = _find_file([
        "Ingredient_Catalog.csv", "ingredient_catalog.csv",
        "Ingredient Catalog.csv",
    ])
    if f:
        try:
            return pd.read_csv(f), f
        except Exception:
            return None, f
    return None, None


def _load_vendors():
    """Load Vendor Contacts. Returns (df, filename) or (None, None)."""
    f = _find_file([
        "Vendor_Contacts___Terms.csv", "Vendor_Contacts_Terms.csv",
        "vendor_contacts_terms.csv", "Vendor Contacts & Terms.csv",
    ])
    if f:
        try:
            return pd.read_csv(f), f
        except Exception:
            return None, f
    return None, None


# ==================================================================
# ASSIGNMENT: Week 1 In-Class Exercise
# ==================================================================
def check_week1_inclass():
    """Ingredient Catalog Viewer - 40 points total."""
    checks = []
    products_df, products_file = _load_products()
    ingredient_df, ingredient_file = _load_ingredients()
    app_code = _read_app_code()

    # 1. Products file loads (5 pts)
    if products_df is not None and len(products_df) >= 5:
        checks.append((
            "Products & Pricing file loads",
            True,
            "Found %s with %d products." % (products_file, len(products_df)),
            5,
        ))
    elif products_file:
        checks.append((
            "Products & Pricing file loads",
            False,
            "File found but could not load or has fewer than 5 rows.",
            5,
        ))
    else:
        checks.append((
            "Products & Pricing file loads",
            False,
            "File not found. Upload Products___Pricing.csv to your repo.",
            5,
        ))

    # 2. Products required columns (5 pts)
    req_prod = ["SKU", "Product Name", "Retail Price"]
    if products_df is not None:
        missing = [c for c in req_prod if c not in products_df.columns]
        if not missing:
            checks.append(("Products has required columns", True,
                           "Columns present: %s." % ", ".join(req_prod), 5))
        else:
            checks.append(("Products has required columns", False,
                           "Missing: %s." % ", ".join(missing), 5))
    else:
        checks.append(("Products has required columns", False,
                        "Cannot check - file not loaded.", 5))

    # 3. Ingredient Catalog loads (5 pts)
    if ingredient_df is not None and len(ingredient_df) >= 30:
        checks.append((
            "Ingredient Catalog file loads",
            True,
            "Found %s with %d ingredients." % (ingredient_file, len(ingredient_df)),
            5,
        ))
    elif ingredient_file:
        checks.append(("Ingredient Catalog file loads", False,
                        "File found but could not load or fewer than 30 rows.", 5))
    else:
        checks.append(("Ingredient Catalog file loads", False,
                        "File not found. Upload Ingredient_Catalog.csv.", 5))

    # 4. Ingredient required columns (5 pts)
    req_ing = ["Ingredient SKU", "Description", "Order Unit",
               "Cost Per Unit", "MOQ", "Primary Supplier ID",
               "Primary Supplier Name"]
    if ingredient_df is not None:
        missing = [c for c in req_ing if c not in ingredient_df.columns]
        if not missing:
            checks.append(("Ingredient Catalog has required columns", True,
                           "All %d columns present." % len(req_ing), 5))
        else:
            checks.append(("Ingredient Catalog has required columns", False,
                           "Missing: %s." % ", ".join(missing), 5))
    else:
        checks.append(("Ingredient Catalog has required columns", False,
                        "Cannot check - file not loaded.", 5))

    # 5. Cost data numeric (5 pts)
    if ingredient_df is not None and "Cost Per Unit" in ingredient_df.columns:
        costs = pd.to_numeric(ingredient_df["Cost Per Unit"], errors="coerce")
        valid = costs.dropna()
        if len(valid) == len(ingredient_df) and valid.min() > 0:
            checks.append(("Cost data is numeric and valid", True,
                           "Range: $%.2f - $%.2f." % (valid.min(), valid.max()), 5))
        else:
            checks.append(("Cost data is numeric and valid", False,
                           "%d rows have missing or non-numeric costs."
                           % (len(ingredient_df) - len(valid)), 5))
    else:
        checks.append(("Cost data is numeric and valid", False,
                        "Cannot check - missing column.", 5))

    # 6. Supplier names available (5 pts)
    if ingredient_df is not None and "Primary Supplier Name" in ingredient_df.columns:
        n = ingredient_df["Primary Supplier Name"].dropna().nunique()
        if n >= 5:
            checks.append(("Supplier data available for filtering", True,
                           "%d unique suppliers in catalog." % n, 5))
        else:
            checks.append(("Supplier data available for filtering", False,
                           "Only %d suppliers - expected at least 5." % n, 5))
    else:
        checks.append(("Supplier data available for filtering", False,
                        "No Primary Supplier Name column found.", 5))

    # 7. Sidebar navigation (5 pts)
    if app_code:
        has_sidebar = "sidebar" in app_code.lower()
        has_nav = any(kw in app_code.lower()
                      for kw in ["radio", "selectbox", "page", "navigation"])
        if has_sidebar:
            checks.append(("App has sidebar navigation", True,
                           "Sidebar navigation detected.", 5))
        else:
            checks.append(("App has sidebar navigation", False,
                           "No sidebar found. Use st.sidebar.radio() or similar.", 5))
    else:
        checks.append(("App has sidebar navigation", False,
                        "No app.py found.", 5))

    # 8. Displays data (5 pts)
    if app_code:
        has_display = any(kw in app_code.lower()
                         for kw in ["dataframe", "table", "plotly", "write("])
        if has_display:
            checks.append(("App displays data", True,
                           "Data display component found.", 5))
        else:
            checks.append(("App displays data", False,
                           "No st.dataframe(), st.table(), or chart found.", 5))
    else:
        checks.append(("App displays data", False, "No app.py found.", 5))

    return checks


# ==================================================================
# ASSIGNMENT: Homework 1 - Supplier Lookup
# ==================================================================
def check_homework1():
    """Supplier Lookup - 45 points total."""
    checks = []
    products_df, _ = _load_products()
    ingredient_df, _ = _load_ingredients()
    vendor_df, vendor_file = _load_vendors()
    app_code = _read_app_code()

    # 1. Vendor file loads (5 pts)
    if vendor_df is not None and len(vendor_df) >= 20:
        checks.append(("Vendor Contacts file loads", True,
                        "Found %s with %d suppliers." % (vendor_file, len(vendor_df)), 5))
    elif vendor_file:
        checks.append(("Vendor Contacts file loads", False,
                        "File found but could not load or fewer than 20 rows.", 5))
    else:
        checks.append(("Vendor Contacts file loads", False,
                        "File not found. Upload Vendor_Contacts___Terms.csv.", 5))

    # 2. Vendor required columns (5 pts)
    req_vendor = ["Supplier ID", "Company Name",
                  "Lead Time (weeks)", "Payment Terms"]
    if vendor_df is not None:
        missing = [c for c in req_vendor if c not in vendor_df.columns]
        if not missing:
            checks.append(("Vendor file has required columns", True,
                           "Key columns present.", 5))
        else:
            checks.append(("Vendor file has required columns", False,
                           "Missing: %s." % ", ".join(missing), 5))
    else:
        checks.append(("Vendor file has required columns", False,
                        "Cannot check - file not loaded.", 5))

    # 3. Shared key links (10 pts)
    if ingredient_df is not None and vendor_df is not None:
        ing_col = "Primary Supplier ID"
        ven_col = "Supplier ID"
        if ing_col in ingredient_df.columns and ven_col in vendor_df.columns:
            ing_ids = set(ingredient_df[ing_col].dropna().unique())
            ven_ids = set(vendor_df[ven_col].dropna().unique())
            matched = ing_ids.intersection(ven_ids)
            unmatched = ing_ids - ven_ids
            if matched and not unmatched:
                checks.append(("Supplier ID shared key links correctly", True,
                               "All %d catalog suppliers found in vendor file."
                               % len(ing_ids), 10))
            elif matched:
                extras = ", ".join(list(unmatched)[:3])
                checks.append(("Supplier ID shared key links correctly", True,
                               "%d matched, %d unmatched: %s."
                               % (len(matched), len(unmatched), extras), 10))
            else:
                checks.append(("Supplier ID shared key links correctly", False,
                               "No IDs match. Check both files use same format "
                               "(e.g., SUP-108).", 10))
        else:
            checks.append(("Supplier ID shared key links correctly", False,
                           "Missing '%s' in catalog or '%s' in vendor file."
                           % (ing_col, ven_col), 10))
    else:
        checks.append(("Supplier ID shared key links correctly", False,
                        "Cannot check - one or both files not loaded.", 10))

    # 4. Lead time valid (5 pts)
    if vendor_df is not None and "Lead Time (weeks)" in vendor_df.columns:
        lt = pd.to_numeric(vendor_df["Lead Time (weeks)"], errors="coerce")
        valid = lt.dropna()
        if len(valid) == len(vendor_df) and valid.min() >= 1:
            checks.append(("Lead time data is valid", True,
                           "Range: %d-%d weeks."
                           % (int(valid.min()), int(valid.max())), 5))
        else:
            checks.append(("Lead time data is valid", False,
                           "Some lead times are missing or invalid.", 5))
    else:
        checks.append(("Lead time data is valid", False,
                        "Cannot check - missing column.", 5))

    # 5. App references supplier data (5 pts)
    if app_code:
        has_ref = any(kw in app_code.lower()
                      for kw in ["vendor", "supplier", "lead time",
                                 "lead_time", "payment terms"])
        if has_ref:
            checks.append(("App references supplier data", True,
                           "Supplier/vendor references found in app code.", 5))
        else:
            checks.append(("App references supplier data", False,
                           "No vendor/supplier references in app.py.", 5))
    else:
        checks.append(("App references supplier data", False,
                        "No app.py found.", 5))

    # 6. Metric display (5 pts)
    if app_code:
        if "metric" in app_code.lower():
            checks.append(("App displays summary metric(s)", True,
                           "st.metric() or metric display found.", 5))
        else:
            checks.append(("App displays summary metric(s)", False,
                           "No st.metric() found. Add total minimum reorder "
                           "cost (sum of Cost x MOQ).", 5))
    else:
        checks.append(("App displays summary metric(s)", False,
                        "No app.py found.", 5))

    # 7. Reorder cost feasible (5 pts)
    if ingredient_df is not None:
        cost_col = "Cost Per Unit"
        moq_col = "MOQ"
        if cost_col in ingredient_df.columns and moq_col in ingredient_df.columns:
            costs = pd.to_numeric(ingredient_df[cost_col], errors="coerce")
            moqs = pd.to_numeric(ingredient_df[moq_col], errors="coerce")
            total = (costs * moqs).sum()
            if total > 0:
                checks.append(("Reorder cost calculation is feasible", True,
                               "Expected total: $%s. Verify your app shows this."
                               % format(total, ",.2f"), 5))
            else:
                checks.append(("Reorder cost calculation is feasible", False,
                               "Calculates to $0 - check Cost and MOQ are numeric.", 5))
        else:
            checks.append(("Reorder cost calculation is feasible", False,
                           "Missing Cost Per Unit or MOQ columns.", 5))
    else:
        checks.append(("Reorder cost calculation is feasible", False,
                        "Cannot calculate - Ingredient Catalog not loaded.", 5))

    # 8. All three files loaded (5 pts)
    files_loaded = sum(1 for df in [products_df, ingredient_df, vendor_df]
                       if df is not None)
    if files_loaded == 3:
        checks.append(("All three data files loaded", True,
                        "Products (%d), Ingredients (%d), Vendors (%d)."
                        % (len(products_df), len(ingredient_df), len(vendor_df)), 5))
    else:
        missing = []
        if products_df is None: missing.append("Products & Pricing")
        if ingredient_df is None: missing.append("Ingredient Catalog")
        if vendor_df is None: missing.append("Vendor Contacts")
        checks.append(("All three data files loaded", False,
                        "Missing: %s." % ", ".join(missing), 5))

    return checks


# ==================================================================
# PUBLIC INTERFACE - called by self_check.py
# ==================================================================
def get_assignments():
    """
    Return a dict of assignment names to check functions.
    The instructor controls what students see by adding/removing
    entries here before releasing the file.

    Each check function returns a list of (name, passed, detail, points).
    """
    return {
        "Week 1 In-Class: Ingredient Catalog Viewer": check_week1_inclass,
        "Homework 1: Supplier Lookup": check_homework1,
    }
