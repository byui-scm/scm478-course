# Week 1, Day 1 — Introduction and Setup

---

## Agenda

1. Course overview and expectations (15 min)
2. Tour of the GitHub repository (10 min)
3. Environment setup check — run `self_check.py` together (15 min)
4. Introduction to Peak Fuel Foods — reading discussion (15 min)
5. Live demo: loading a CSV and displaying it in Streamlit (20 min)
6. Q&A and assignment overview (5 min)

---

## Setup Check

Before class starts, make sure you have completed all steps in [getting-started.md](../../setup/getting-started.md).

During class, run:
```bash
python setup/self_check.py
```

If it passes, you are ready. If not, we will troubleshoot together.

---

## Introduction to Streamlit

Streamlit is a Python library that turns scripts into interactive web apps. The core pattern:

```python
import streamlit as st
import pandas as pd

df = pd.read_csv("data/Products___Pricing.csv")
st.title("Peak Fuel Products")
st.dataframe(df)
```

Run with:
```bash
streamlit run app.py
```

---

## Your First App

By the end of today's demo, you will have a working app that:
- Loads `Products___Pricing.csv`
- Displays it as a table
- Has a title and a brief description

This is the foundation for everything you build in Weeks 1–3.

---

## Before Day 2

- Re-read the Streamlit docs section on `st.dataframe` and `st.sidebar`
- Look through `data/Ingredient_Catalog.csv` — what would you want to filter by?
- Complete any remaining setup steps
