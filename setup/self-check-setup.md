# Week 01 - Adding the Self-Check Module to Your App

## Adding the Self-Check Module to Your App
**SCM 478 — Setup Guide**

Do this once at the start of the semester. New check files will be added each unit.

---

## What the Self-Check Does

The Self-Check is a page in your app that automatically tests whether your app meets the assignment requirements. Each check tells you:

- What's being checked (e.g., "Ingredient Catalog file loads")
- Whether it passes (green check or red X)
- How many points it's worth (matches the rubric)
- What's wrong if it fails (e.g., "File not found. Upload Ingredient_Catalog.csv.")

It does NOT tell you how to fix the problem — that's your job. It tells you what the problem is and how much it costs.

Run the Self-Check every time you make a change. Your goal is 100% before you submit.

---

## File Structure

Your repo should look like this after setup:

```
scm478-peak-fuel/

  app.py                           <- your main app
  self_check.py                    <- self-check page (add once, never change)
  requirements.txt                 <- streamlit, pandas, plotly
  checks/
    __init__.py                    <- makes checks/ a Python package
    unit1_checks.py                <- Unit 1 checks (Weeks 1-4)
  Products___Pricing.csv           <- data file (Week 1)
  Ingredient_Catalog.csv           <- data file (Week 1)
  Vendor_Contacts___Terms.csv      <- data file (Homework 1)
```

As the semester progresses, new check files are released:

```
checks/
  __init__.py
  unit1_checks.py     <- released Week 1
  unit2_checks.py     <- released Week 5
  unit3_checks.py     <- released Week 8
  unit4_checks.py     <- released Week 11
```

Each new file adds checks for that unit's assignments. Previous checks remain — if you break something from an earlier week, you'll see it.

---

## Step-by-Step Setup

### Step 1: Download the self-check files

Your instructor will provide three files. Download them:

- `self_check.py`
- `checks/__init__.py`
- `checks/unit1_checks.py`

### Step 2: Upload to your GitHub repo

1. Go to your GitHub repo in your browser
2. Upload `self_check.py` to the root of your repo (same level as `app.py`)
3. Create the `checks` folder and add `__init__.py`:
   - Click **Add file** → **Create new file**
   - In the filename field, type `checks/__init__.py`
   - Paste the contents of `__init__.py`
   - Click **Commit changes**
4. Add the Unit 1 checks:
   - Click **Add file** → **Create new file**
   - In the filename field, type `checks/unit1_checks.py`
   - Paste the contents of `unit1_checks.py`
   - Click **Commit changes**

### Step 3: Add Self-Check to your app's navigation

In your `app.py`, add `"Self-Check"` as a sidebar navigation option. Here's the pattern:

```python
import self_check

# In your sidebar navigation:
page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Ingredients", "Sales", "Purchasing", "Self-Check"]
)

# In your page routing:
if page == "Self-Check":
    self_check.run_self_check()
elif page == "Dashboard":
    # ... your dashboard code
elif page == "Ingredients":
    # ... your ingredients code
# ... etc.
```

### Step 4: Commit and verify

1. Commit your changes to GitHub
2. Wait for Streamlit to redeploy (30–60 seconds)
3. Click **Self-Check** in your sidebar
4. You should see the check results

---

## How to Use Self-Check During Development

1. Build one feature (e.g., load the Ingredient Catalog)
2. Commit to GitHub
3. Wait for Streamlit to redeploy (30–60 seconds)
4. Click **Self-Check** in your sidebar
5. Read the results — find the first red X
6. Fix that one issue
7. Repeat until everything is green

Don't try to fix everything at once. Fix one thing, commit, check.

---

## How Grading Works

The Self-Check percentage IS your score for Module Builds, subject to two conditions:

1. Self-Check shows 100% on the relevant section
2. The app actually works when the instructor clicks through it (filters filter, charts display, metrics show correct values)

The self-check verifies that the right files are loaded, the right columns exist, and the right data connections are in place. It cannot verify that your UI works correctly — that's your responsibility.

If Self-Check shows 100% but the app doesn't work visually, the instructor will ask you to resubmit.

---

## Adding New Unit Checks

When a new unit begins, your instructor will release a new check file (e.g., `unit2_checks.py`). To add it:

1. Download the file
2. Upload it to the `checks/` folder in your GitHub repo
3. Commit

The Self-Check page will automatically discover and display the new checks. You don't need to change `self_check.py` or `app.py` — the system discovers new check files automatically.

---

## Troubleshooting

**"No check modules found"**
The `checks/` folder is missing or empty. Make sure you have `checks/__init__.py` and `checks/unit1_checks.py` in your repo.

**File-not-found errors for CSV files**
The check is looking for specific filenames. Make sure your CSV files are named exactly as expected (e.g., `Ingredient_Catalog.csv`, not `ingredient-catalog.csv`). Check capitalization and underscores.

**Checks pass but app looks broken**
The self-check validates data structure, not visual layout. If your data loads correctly but the page looks wrong, the issue is in your display code — ask AI to help fix the layout.

**Self-Check page doesn't appear in sidebar**
Make sure you imported `self_check` at the top of `app.py` and added the `"Self-Check"` option to your sidebar navigation. See Step 3 above.
