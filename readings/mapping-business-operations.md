# Mapping Business Operations

*Read before Week 1.*

---

## Purpose

Before you can build a tool for a business, you need to understand how that business actually works. This reading introduces a simple framework for mapping the operational processes you will encounter throughout this course.

---

## The Three Questions

When approaching any new business scenario — in homework, on transfer exams, or in your career — start by answering three questions:

1. **What flows?** Identify the primary objects moving through the system: products, ingredients, orders, purchase orders, cash.
2. **Where does it go?** Map the sequence of steps: supplier → receiving → inventory → production → finished goods → customer.
3. **What can go wrong?** Every useful SCM tool is built around a risk: a shortage, a delay, a forecast miss, a bottleneck.

---

## Applying the Framework to Peak Fuel Foods

*[Instructor will add worked example here showing how Products, Ingredients, Vendors, POs, and Sales all connect in the Peak Fuel data model.]*

---

## The Data Model

A supply chain data model answers: *what are the entities, and how do they relate?*

```
Vendors ──supplies──> Ingredients ──used in──> Products
   |                       |
   └── Purchase Orders      └── Inventory Count
           |
           └── Receiving Log

Products ──sold via──> Sales Log
```

This is the structure you will work with in Weeks 1–3.

---

## Checkpoint

Before Week 1, you should be able to open each CSV in the `data/` folder and describe in one sentence what it contains and how it connects to at least one other file.
