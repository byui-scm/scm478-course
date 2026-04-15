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

Let's apply the three questions to Maria's business.

**What flows?**
The primary objects moving through Peak Fuel's system are: raw ingredients (from suppliers into inventory), finished products (from production into finished goods), purchase orders (from Maria to suppliers), sales orders (from retailers to Maria), and cash (in both directions).

**Where does it go?**
```
Suppliers → PO → Receiving → Ingredient Inventory
                                      ↓
                             Production (Recipes apply)
                                      ↓
                           Finished Product Inventory
                                      ↓
                             Retailers / Consumers → Sales Log
```

**What can go wrong?**
Maria's answer to this question is the entire premise of this course:
- A supplier is late → she doesn't know which products are affected
- Demand spikes → she doesn't know if she has enough ingredients
- She runs out of a key ingredient mid-week → she finds out when production starts, not Friday when she could have reordered
- A retailer asks for a trace-back → she can't connect a finished burrito to the shipment of chicken that went into it

Every tool you build this semester is a direct response to one of these risks.

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
