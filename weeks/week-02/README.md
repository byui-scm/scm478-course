# Week 2 — Peak Fuel Sales and Demand (Multi-Source + Charts)

**Theme:** Move from displaying data to reading it. Turn eleven weeks of sales into a picture Maria can act on.

---

## Learning Objectives

- Aggregate transactional data into weekly summaries
- Build interactive trend charts with Plotly
- Add multi-dimensional filters (channel, customer)
- Display period-over-period change with `st.metric()` deltas
- Distinguish demand signals from noise in a short sales history

---

## Files This Week

| File | Description |
|------|-------------|
| [day3-exercise.md](day3-exercise.md) | Day 3: Design exercise + begin Sales and Demand build |
| [day4-exercise.md](day4-exercise.md) | Day 4: Complete the build + SCM interpretation discussion |
| [homework2.md](homework2.md) | Homework 2: Inventory alerts with weeks-of-supply |

The Day 3 Readiness Assurance Test is administered in LAMS (iRAT + tRAT). It covers the demand-signals reading.

---

## Before Day 3 (Assigned End of Week 1)

1. Complete the Self-Check setup homework (from Week 1)
2. Read [Reading Demand Signals](../../readings/demand-signals.md)

The Day 3 RAT in LAMS covers the reading. Come prepared.

---

## Data Files Added This Week

- `data/Sales Log.csv` (143 transactions, 11 weeks) — added Day 3
- `data/Inventory Count.csv` (33 ingredients, counted 03/27/2026) — added in Homework 2
- `data/Recipes & Ingredients.csv` (56 BOM rows) — added in Homework 2

---

## How This Fits the Big Picture

Week 1 asked "what do we have?" Week 2 asks "what is happening?"

You are still in the **descriptive** layer of operational visibility, but you are making it dynamic. A sales trend chart answers questions that a static catalog cannot: What is growing? What is shrinking? What surprises the founder when she sees it?

The interpretation skill you build this week sets up the forecasting work in Unit 2, where you will turn these patterns into quantitative predictions.

---

## Spiritual Theme

**Demand Signals — Discernment over Wishful Thinking.** Joseph in Egypt read the signs of the times, prepared before the crisis, and used information to bless the people around him. This week, you practice the same discipline in miniature: read the data honestly, prepare before the shortage, act on what is true rather than what you wish were true.
