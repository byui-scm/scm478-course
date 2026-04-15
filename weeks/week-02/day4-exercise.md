# Day 4 — Finish the Sales and Demand View + What the Data Says

**Time:** ~75 minutes of active work + 15 minutes of discussion
**Submission:** Final Sales and Demand page committed before end of class. This becomes **Module Build 2**.

---

## Opening (10 minutes)

Your instructor will walk around and spot-check your Day 3 progress. Use this time to:

- Pull your teammates' GitHub repos and see how other teams structured the pivot
- Ask questions about anything that broke between classes
- Fix any errors that came up when you pushed last time

---

## Part 1 — Add Charts (20 minutes)

Install Plotly if you haven't already:

```bash
pip install plotly
```

Add to `requirements.txt`:

```
plotly
```

Build a **weekly trend chart** that shows all five products as lines over the eleven-week window. Each line uses a distinct color. The x-axis is the week number (or week-start date), the y-axis is units sold.

Requirements:

- Use `plotly.express.line()` or `plotly.graph_objects`
- Chart title: "Weekly Units by Product"
- Hover tooltip shows product name, week, and units
- The chart updates when the user applies filters (next section)

Do not go fancy. A clean line chart beats a confused stacked bar chart every time.

---

## Part 2 — Add Filters (15 minutes)

Add two sidebar filters that apply to the trend chart and the weekly pivot:

1. **Channel filter** — multi-select: Retail, Wholesale, Direct. Default = all selected.
2. **Customer filter** — multi-select showing every unique customer in the sales log. Default = all selected.

When the user changes either filter, both the chart and the pivot table recompute.

**Prompting tip:** Start by asking the AI for a pattern like "how do I filter a DataFrame by a multiselect in Streamlit" before integrating it into your page. Understanding the pattern in isolation is faster than debugging it inside a larger function.

---

## Part 3 — Metric Cards with Delta (15 minutes)

Above the chart, display five `st.metric()` cards in a row — one per product. Each card shows:

- **Label:** Product name
- **Value:** Last week's units sold
- **Delta:** Change from the prior week (positive = up arrow green, negative = down arrow red)

Use `st.columns(5)` to lay them out horizontally. `st.metric()` has a `delta` argument that handles the arrow automatically.

---

## Part 4 — The Interpretation Discussion (20 minutes, full class)

Close your laptops. Your instructor will run this as a whole-class discussion with cold-called teams.

**The setup.** You are now staring at eleven weeks of Peak Fuel sales data. The data reveals what Maria's gut would not:

- Original Protein Burrito: highest volume, steady growth
- Green Fuel Smoothie Pack: up ~84% — fastest percentage growth
- Sunrise Breakfast Wrap: growing modestly
- Protein Power Bowl: declining
- Peak Bar: flat or declining

**The questions.**

1. If you were Maria, which of these trends would change your production plan for next week? Why?
2. Which of these trends might be **noise** rather than **signal**? How would you test your guess?
3. Your data shows the Power Bowl declining. What are three possible business explanations for that decline, and which one would you investigate first?
4. The Smoothie Pack's 84% growth looks exciting. Name one reason it might be misleading. (Hint — revisit the data gap discussion in the reading.)
5. If Maria asked you *right now*: "How many Smoothie Packs should I make next week?" — what would you answer, and what would you need to know that the data alone cannot tell you?

The point of this discussion is not to get the "right" answer. The point is to practice the judgment layer that sits on top of the data. Every week in this course, you will build something that produces numbers. Knowing what to do with those numbers is the skill your future employer is paying for.

---

## Part 5 — Preview of Homework 2 (5 minutes)

Homework 2 extends what you built today. Maria's next question:

> "I spend every Friday afternoon counting inventory and trying to figure out if I have enough of everything for next week. Can you build something that tells me which ingredients are running low based on what we've been selling?"

You will connect the sales trends you just built to the Bill of Materials (`Recipes & Ingredients.csv`) and the current inventory count, and flag ingredients that are running short. See [homework2.md](homework2.md).

---

## End-of-Class Checkpoint — Module Build 2

- [ ] Weekly trend chart shows five product lines
- [ ] Channel filter and customer filter both affect the chart and pivot
- [ ] Five metric cards with delta arrows display last-week vs. prior-week
- [ ] Self-Check shows 100% on the "Module Build 2" section
- [ ] Code committed with message `"Module Build 2 complete"`
- [ ] GitHub link and live Streamlit URL posted on Canvas
