# Reading Demand Signals

*Unit 1, Week 2 — SCM 478*

---

## What Sales Data Is (and Isn't)

A sales log is a history book. Every row is a transaction that already happened: someone bought something, at some price, on some day, through some channel. That history is valuable — but only if you read it carefully.

Sales data is **not** a forecast. It tells you what customers did last week. It does not tell you what they will do next week. A customer who bought 40 burritos on Monday did so because of reasons the data does not record: a promotion, a weather pattern, a referral from another store, a weekend event. Strip those reasons out and you are left with a number. Numbers without context are dangerous; numbers with context are a starting point for judgment.

Maria's instinct — "the Original Protein Burrito is our best seller" — is the kind of claim that data either confirms or corrects. Either way, the job of a supply chain analyst is to replace gut feeling with visibility, and then replace visibility with disciplined interpretation.

---

## Signal vs. Noise

Any weekly sales number has two ingredients:

- **Signal** — the real underlying pattern (a product is growing because demand is shifting toward it)
- **Noise** — the random variation (a retailer placed a one-time stock-up order, a storm closed a store for two days, a customer double-ordered by mistake)

If you react to noise as if it were signal, you will whipsaw your operation: order too much, cut too much, panic, relax, panic again. If you ignore signal because it looks like noise, you will miss the shift until it's too late to respond.

How do you tell them apart? A few heuristics:

1. **Aggregate.** Daily numbers are noisy. Weekly numbers are less noisy. Monthly numbers are smoother still. The right level depends on how fast your decisions need to move.
2. **Look for direction, not magnitude.** If sales have climbed for six straight weeks, that is a signal even if week six was lower than week five. One-week movements mean almost nothing.
3. **Compare channels.** If a trend shows up in Retail *and* Wholesale *and* Direct, it is likely real. If it shows up in only one channel, it may be that channel is doing something unusual.
4. **Distrust short histories.** Eleven weeks of data is not enough to be confident about anything. It is enough to form a hypothesis and test it against next week's numbers.

---

## Four Questions Sales Data Can Answer

| Question | What you look at |
|----------|------------------|
| What sold? | Total units by product over a period |
| What is growing? | Week-over-week direction and percentage change |
| Where did it sell? | Aggregations by channel or customer |
| Who are the biggest buyers? | Ranked customer totals |

Notice what is missing from this list: *why* it sold, *whether* it will sell again, and *how much* to make next week. Those are all judgment questions. The data supports the judgment. It does not replace it.

---

## Demand Signals for Peak Fuel Foods

Peak Fuel has about eleven weeks of sales history. Over that window, the data tells a clear story if you read it honestly:

- **Original Protein Burrito** is the highest-volume product and growing steadily. Maria's gut is right.
- **Green Fuel Smoothie Pack** is growing fastest in percentage terms (up roughly 84% over the window). Maria has not noticed yet because the absolute numbers are still small.
- **Protein Power Bowl** is declining. Maria may be defending a product that customers are leaving.
- **Peak Bar** is flat or slightly declining.
- **Sunrise Breakfast Wrap** is growing modestly.

Every one of these observations has operational consequences: how much to produce next week, which ingredients to prioritize, which supplier relationships matter most, and — eventually — which product line to expand or retire. None of those decisions belong to the data alone. But none of them can be made well without the data.

---

## The Data Gap

Sales data tells you *what customers bought*. It does not tell you *what customers wanted*. If Peak Fuel stocks out of Smoothie Packs on Tuesday, that lost sale never shows up in the sales log. The log shows zero sales — indistinguishable from a week where no one wanted the product at all.

This is one of the most important things to understand about any sales dataset: **stockouts hide in the silence**. A product that looks flat in the data may actually be growing faster than anything else in your catalog — you just can't see it because you keep running out.

Later in the course, you will build tools that compare sales against inventory availability to catch this. For now, just know it is there.

---

## Discussion Questions

1. Maria is about to set next week's production based on the last four weeks of sales. Which of the heuristics above would you use to decide whether to trust the numbers?
2. Suppose the Smoothie Pack shows +84% growth over eleven weeks. How confident should Maria be that the trend continues? What additional evidence would raise or lower your confidence?
3. Why is a channel filter (Retail / Wholesale / Direct) useful for reading demand signals, even if Maria only cares about total units sold?
4. Imagine you see a week with unusually high sales. Describe two ways to tell whether it is signal or noise without leaving the data.
5. What is one piece of information that would dramatically change how you read Peak Fuel's sales log — something the log does not currently contain?
