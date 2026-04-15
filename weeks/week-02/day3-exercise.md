# Day 3 — In-Class Exercise: Begin the Sales and Demand View

**Time:** ~55 minutes (after self-check debrief and RAT)
**Submission:** Commit what you have at the end of class. You will finish on Day 4.

---

## Maria's Question

> "I need to see what's selling. Which products are growing? Which are flat? I make ordering decisions based on gut feel right now — I want to see the actual numbers."

She hands you a new file: [Sales Log.csv](https://git-link.vercel.app/api/download?url=https%3A%2F%2Fgithub.com%2Fbyui-scm%2Fscm478-course%2Fblob%2Fmain%2Fdata%2F&filename=Sales_Log.csv). It contains 143 transactions spread across eleven weeks, five products, and three sales channels.

---

## Part 1 — Verbal Design (10 minutes, in teams)

**Before you touch any code or any AI assistant, answer these four questions on paper or whiteboard as a team.** Your instructor will call on one team per question.

1. **Inputs** — What data do you need to answer Maria's question? Which files? Which columns from each file?
2. **Calculation** — What math must happen to turn 143 transaction rows into something Maria can read? Be specific — what are you grouping by, and what are you summing?
3. **Output** — What does Maria actually see on the screen? A chart? A table? A number? All three? Describe the layout in one sentence per element.
4. **Edge cases** — What could go wrong with this data? What should happen if a week has no sales for a product? What if a customer name is mistyped?

Only after your team has answered all four questions should you open Cursor or Claude.

---

## Part 2 — Build: Weekly Aggregation and Basic Trend Table (45 minutes)

### Starting Point

Open the `app.py` you built in Week 1. Add a new tab (or sidebar page) called **Sales and Demand**.

### Required Features for Day 3

You must finish these before the end of class. Day 4 adds charts, filters, and metrics.

1. **Load the data.** Read `data/Sales Log.csv` into a DataFrame. Parse the `Date` column as a real date.
2. **Compute weekly totals by product.** Aggregate the sales log so that you have one row per product per ISO week showing total units sold and total revenue (quantity × unit price).
3. **Display a pivot table.** Show weekly units in a format Maria can scan: products as rows, weeks as columns, units in the cells. Highlight the two highest-growth products.
4. **Add a quick-scan summary.** Below the pivot, display the five products as a simple ranked list: product name, total units over the eleven weeks, and one-sentence description of the trend (growing, declining, flat).

### AI Prompting Guidance (Medium Scaffolding)

You are writing your own prompts this week. A good prompt for this exercise has four parts:

1. **Context:** "I'm building a Streamlit app for a small food company called Peak Fuel Foods."
2. **Data description:** The file path, column names, and one or two example rows.
3. **Goal:** What you want the user to see and what calculation produces it.
4. **Constraints:** Use Pandas. Don't use any libraries beyond pandas and streamlit yet. Pure Python where possible.

**Do not prompt the AI to "build the Sales and Demand page."** That is too vague. Break the work into the four required features above and prompt one feature at a time. If your AI produces code you don't understand, stop and ask it to explain each line before moving on.

---

## End-of-Class Checkpoint

Before you leave:

- [ ] Your app loads `Sales Log.csv` without errors
- [ ] Weekly totals display in a readable format
- [ ] The ranked product list appears
- [ ] Code committed with message like `"Day 3: add sales weekly aggregation"`
- [ ] GitHub link posted on Canvas

---

*Day 4 will add charts, filters, metrics, and the interpretation discussion. See [day4-exercise.md](day4-exercise.md).*
