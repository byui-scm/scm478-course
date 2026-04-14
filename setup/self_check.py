"""
SCM 478 Environment Self-Check
Run from the repo root: python setup/self_check.py
"""

import sys
import importlib
import os
from pathlib import Path

PASS = "[PASS]"
FAIL = "[FAIL]"

results = []


def check(label, ok, hint=""):
    status = PASS if ok else FAIL
    msg = f"{status} {label}"
    if not ok and hint:
        msg += f"\n       Hint: {hint}"
    results.append((ok, msg))
    print(msg)


print("SCM 478 Environment Self-Check")
print("=" * 40)

# Python version
major, minor = sys.version_info[:2]
py_ok = major == 3 and minor >= 10
check(
    f"Python version: {major}.{minor}.{sys.version_info[2]}",
    py_ok,
    "Install Python 3.10 or later from python.org",
)

# Required packages
for package, install_name in [
    ("pandas", "pandas"),
    ("streamlit", "streamlit"),
    ("matplotlib", "matplotlib"),
]:
    try:
        mod = importlib.import_module(package)
        version = getattr(mod, "__version__", "unknown")
        check(f"{package} installed: {version}", True)
    except ImportError:
        check(
            f"{package} installed",
            False,
            f"Run: pip install {install_name}",
        )

# data/ folder
repo_root = Path(__file__).parent.parent
data_dir = repo_root / "data"
check(
    "data/ folder found",
    data_dir.is_dir(),
    f"Expected at: {data_dir}",
)

# Unit checks
checks_dir = Path(__file__).parent / "checks"
unit_check_files = sorted(checks_dir.glob("unit*_checks.py")) if checks_dir.exists() else []

if unit_check_files:
    for check_file in unit_check_files:
        unit_name = check_file.stem.replace("_", " ").title()
        try:
            spec = importlib.util.spec_from_file_location(check_file.stem, check_file)
            mod = importlib.util.module_from_spec(spec)
            mod.REPO_ROOT = repo_root
            spec.loader.exec_module(mod)
            errors = mod.run_checks()
            if errors:
                for err in errors:
                    check(f"{unit_name}: {err}", False)
            else:
                check(f"{unit_name}: all passed", True)
        except Exception as e:
            check(f"{unit_name}: error running checks", False, str(e))
else:
    print("[INFO] No unit checks found in setup/checks/")

# Summary
print()
passed = sum(1 for ok, _ in results if ok)
total = len(results)
if passed == total:
    print("All checks passed. You are ready for class.")
else:
    print(f"{passed}/{total} checks passed. See hints above.")
    sys.exit(1)
