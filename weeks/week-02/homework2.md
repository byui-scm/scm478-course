# Homework 2 — Peak Fuel Inventory Alerts

**Due:** See Canvas
**Points:** 10

---

## Maria's Question

> "I spend every Friday afternoon counting inventory and trying to figure out if I have enough of everything for next week. Can you build something that tells me which ingredients are running low based on what we've been selling?"

---

## What You Are Building

A new page in your app called **Inventory Alerts**. It connects three files — the sales log you already loaded, the inventory count, and the recipe-to-ingredient BOM — to produce a weeks-of-supply view. The page flags ingredients that are running short based on recent sales pace.

This is the first homework in the course that requires you to *calculate* something non-trivial from multiple data sources. Take your time with the design before you start prompting.

---

## New Data Files

Copy these two files into your `data/` folder:

- `data/Inventory Count.csv` (33 ingredients, counted 03/27/2026)
- `data/Recipes & Ingredients.csv` (56 BOM rows linking products to ingredients)

---

## Requirements

### Requirement 1 — Compute Weekly Ingredient Consumption (3 pts)

For each ingredient in the BOM, calculate how much of it Peak Fuel consumes in an average week based on the last four weeks of sales.

**The math:**

```
weekly ingredient demand =
  sum over all products of
    (average weekly units sold of that product) × (qty per unit from BOM)
```

Example: If Original Protein Burrito averaged 200 units per week for the last four weeks, and the BOM says each burrito uses 0.1 of a Yellow Onion, that's 20 onions per week from that product alone. Add up the contribution from every product that uses Yellow Onions to get total weekly onion demand.

**Ignore yield factors for this homework.** You will add them later in the course.

### Requirement 2 — Weeks of Supply Column (3 pts)

For each ingredient, compute:

```
weeks of supply = on_hand_qty / weekly_ingredient_demand
```

Display a table with one row per ingredient showing:

- Ingredient SKU
- Description
- On Hand Qty
- Weekly Demand (computed above)
- Weeks of Supply (rounded to 1 decimal)

Handle the edge case: if weekly demand is zero (the ingredient is in the catalog but no product uses it), show "N/A" in the Weeks of Supply column rather than dividing by zero.

### Requirement 3 — Threshold Alerts (2 pts)

Color-code or flag the rows:

- **Critical** (red): Weeks of Supply < 1.0
- **Low** (yellow): Weeks of Supply between 1.0 and 2.0
- **OK** (green or no color): Weeks of Supply ≥ 2.0

At the top of the page, display a summary like:

> 3 ingredients are CRITICAL. 7 ingredients are LOW. 21 ingredients are OK. 2 ingredients have no demand.

### Requirement 4 — The Judgment Question (2 pts)

Below the table, add a short text response (3-5 sentences) to this question and display it using `st.info()` or `st.markdown()`:

> Of the ingredients flagged as Critical or Low, which one would you tell Maria to deal with first? Why? What other information would you need to be sure?

This is a written answer, not a calculation. You are practicing the judgment layer from the Day 4 discussion. Grading rewards clear thinking over clever code.

---

## Self-Check

Your Self-Check module has been updated with new checks for Homework 2. Run it after each change. Aim for 100% on the "Homework 2" section before submitting.

---

## Submission

1. Push your updated `app.py` to your GitHub repo
2. Verify the live Streamlit deployment updates
3. Submit both the GitHub link and the Streamlit URL on Canvas

---

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| Weekly ingredient demand calculated correctly from sales + BOM | 3 |
| Weeks of Supply column with divide-by-zero handling | 3 |
| Threshold alerts with summary count | 2 |
| Written judgment answer (Requirement 4) | 2 |
| **Total** | **10** |

---

## Hints

- Load all three files once at the top of your page. Don't read them inside a loop.
- Use `pd.merge()` to join the sales log to the BOM on `Product SKU`.
- The BOM is one row per product-ingredient pair. An ingredient appears in multiple rows because multiple products use it. `groupby("Ingredient SKU").sum()` is your friend.
- For the "last four weeks" window, filter the sales log to dates within 28 days of the most recent sale before aggregating.
- Test your calculation on a single ingredient by hand before trusting the full output. Pick Yellow Onions and verify the number with a calculator.
