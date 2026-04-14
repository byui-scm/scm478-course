# Self-Check Setup

The self-check script verifies that your environment is correctly configured before you start each unit. Run it whenever you're not sure if your setup is working.

---

## Running the Self-Check

From the root of the course repository, with your virtual environment activated:

```bash
python setup/self_check.py
```

---

## Expected Output (Passing)

```
SCM 478 Environment Self-Check
================================
[PASS] Python version: 3.11.x
[PASS] pandas installed: 2.x.x
[PASS] streamlit installed: 1.x.x
[PASS] matplotlib installed: 3.x.x
[PASS] data/ folder found
[PASS] Unit 1 checks: all passed

All checks passed. You are ready for class.
```

---

## If a Check Fails

Each failure message includes a hint. Common fixes:

| Failure | Fix |
|---------|-----|
| `pandas not installed` | Run `pip install pandas` (make sure your venv is active) |
| `streamlit not installed` | Run `pip install streamlit` |
| `data/ folder not found` | Make sure you are running from the repo root, not the `setup/` folder |
| `Python version too old` | Install Python 3.10 or later from python.org |

---

## Unit-Specific Checks

As the semester progresses, unit-specific checks will be added to `setup/checks/`. Running `self_check.py` automatically runs all available unit checks.

Current checks:
- `unit1_checks.py` — verifies Week 1 data files are present and readable

---

## Getting Help

If your self-check fails and you cannot resolve it with the table above, post in the Canvas discussion board and include:
1. The full output of `python setup/self_check.py`
2. The output of `python --version`
3. Your operating system (Windows/Mac/Linux)
