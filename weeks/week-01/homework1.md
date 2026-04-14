# Homework 1: Peak Fuel Supplier Lookup

**SCM 478 — Due before Week 2, Day 1**  
**Deliverable:** Module Build 1 — Deployed app URL submitted via Canvas

---

## Maria's Question

> "When I'm about to place an order on Friday, I pull up my ingredient catalog to see what I need. But then I have to open a completely separate sheet to find the supplier's phone number, their lead time, and whether they want payment on delivery or net-30. It takes forever to cross-reference. Can you add the supplier information right alongside the ingredient so I can see everything in one place?"

---

## Your Task

Add the supplier data file (`Vendor_Contacts___Terms.csv`) to your Peak Fuel app. When Maria selects an ingredient or filters by supplier, the app should display the supplier's contact information, lead time, and payment terms alongside the ingredient data.

### What to add:

1. **Upload** `Vendor_Contacts___Terms.csv` to your GitHub repo (24 suppliers with Supplier ID, Company Name, Contact Person, Email, Phone, Lead Time in weeks, and Payment Terms).

2. **Connect** the Vendor Contacts data to the Ingredient Catalog using the shared field: `Primary Supplier ID` in the ingredient catalog matches `Supplier ID` in the vendor contacts file.

3. **Display** supplier details (contact name, phone, email, lead time, payment terms) when an ingredient is selected or a supplier is filtered.

4. **Add a summary metric:** Show the total minimum reorder cost — calculated as the sum of (Cost Per Unit × MOQ) across all ingredients. This gives Maria a rough sense of the minimum she'd spend if she had to reorder everything at once.

---

## How to Approach This

Use AI. Describe what you need in plain English. A prompt like this would work:

> "I have an existing Streamlit app that displays an ingredient catalog filtered by supplier. I'm adding a new CSV file called `Vendor_Contacts___Terms.csv` with columns: Supplier ID, Company Name, Contact Person, Email, Phone, Lead Time (weeks), Payment Terms, Notes. I need to join this with my Ingredient_Catalog.csv using the Supplier ID field, and display the supplier's contact info, lead time, and payment terms alongside each ingredient. Also add a metric showing the total minimum reorder cost (sum of Cost Per Unit × MOQ for all ingredients)."

But you should also think about the SCM question *before* prompting: What does Maria actually need to see when she's about to place an order? Is there information in the vendor file that would change her decision about *when* or *how much* to order?

---

## What to Submit

- Your deployed Streamlit app URL (the same URL from class, now updated with the supplier data)
- The app should have a working Ingredients page that shows ingredient data connected to supplier data, with the reorder cost metric

---

## SCM Concept: Data Joins

You just built the same thing that every ERP system does automatically: connecting master data tables through shared keys. In SAP, the ingredient catalog and the supplier master are separate tables linked by a vendor number. In Maria's Google Sheets, they're separate files with no automatic connection. Your app creates that connection.

The supplier's lead time is especially important. If Maria's chicken supplier has a 1-week lead time and her protein powder supplier has a 3-week lead time, she needs to order the protein powder two weeks earlier than the chicken — even if she discovers both shortages on the same Friday. That lead time data, sitting right next to the ingredient, changes the timing of her decisions. We'll use this concept more in Weeks 3 and beyond.
