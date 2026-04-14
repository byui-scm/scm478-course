# Peak Fuel Foods — Data Dictionary

All CSV files for the course live in this folder. Do not modify the original files — copy them into your project folder when building assignments.

---

## Files Overview

| File | Rows | Description |
|------|------|-------------|
| [Products___Pricing.csv](#products___pricingcsv) | 5 | Product catalog with retail pricing |
| [Ingredient_Catalog.csv](#ingredient_catalogcsv) | 33 | Ingredient master list with supplier and cost data |
| [Vendor_Contacts___Terms.csv](#vendor_contacts___termscsv) | 24 | Supplier contact information and payment terms |
| [Sales_Log.csv](#sales_logcsv) | 143 | Sales transactions by date, customer, and channel |
| [Inventory_Count.csv](#inventory_countcsv) | 33 | Most recent physical inventory count |
| [Recipes___Ingredients.csv](#recipes___ingredientscsv) | 56 | Bill of materials (BOM) for each product |
| [PO_Tracker.csv](#po_trackercsv) | 46 | Purchase orders with status and delivery tracking |
| [Receiving_Log.csv](#receiving_logcsv) | 10 | Goods received against purchase orders |

---

## File Details

### Products___Pricing.csv

**5 rows** | Used in: Week 1+

| Column | Description |
|--------|-------------|
| SKU | Unique product identifier |
| Product Name | Full product name |
| Description | Short product description |
| Category | Product category (e.g., Bar, Drink) |
| Unit of Measure | How the product is sold (e.g., each, case) |
| Retail Price | Retail price per unit |

---

### Ingredient_Catalog.csv

**33 rows** | Used in: Week 1+

| Column | Description |
|--------|-------------|
| Ingredient SKU | Unique ingredient identifier |
| Description | Ingredient name and description |
| Order Unit | Unit in which the ingredient is ordered |
| Cost Per Unit | Cost per order unit |
| MOQ | Minimum order quantity |
| Primary Supplier ID | Supplier ID from Vendor_Contacts___Terms.csv |
| Primary Supplier Name | Supplier name |

---

### Vendor_Contacts___Terms.csv

**24 rows** | Used in: Homework 1+

| Column | Description |
|--------|-------------|
| Supplier ID | Unique supplier identifier |
| Company Name | Supplier company name |
| Contact Person | Primary contact name |
| Email | Contact email address |
| Phone | Contact phone number |
| Lead Time (weeks) | Typical order lead time in weeks |
| Payment Terms | Payment terms (e.g., Net 30) |
| Notes | Additional supplier notes |

---

### Sales_Log.csv

**143 rows** | Used in: Week 2+

| Column | Description |
|--------|-------------|
| Date | Transaction date |
| Customer | Customer name or account |
| Product SKU | Product SKU from Products___Pricing.csv |
| Product Name | Product name |
| Quantity | Units sold |
| Unit Price | Price per unit at time of sale |
| Channel | Sales channel (e.g., Retail, Online, Wholesale) |

---

### Inventory_Count.csv

**33 rows** | Used in: Homework 2+

| Column | Description |
|--------|-------------|
| Ingredient SKU | Ingredient SKU from Ingredient_Catalog.csv |
| Description | Ingredient description |
| On Hand Qty | Quantity on hand at count date |
| Unit | Unit of measure |
| Count Date | Date the physical count was taken |
| Location | Storage location in the facility |
| Notes | Count notes or discrepancies |

---

### Recipes___Ingredients.csv

**56 rows** | Used in: Homework 2+, Week 9

| Column | Description |
|--------|-------------|
| Product SKU | Product SKU from Products___Pricing.csv |
| Product Name | Product name |
| Ingredient SKU | Ingredient SKU from Ingredient_Catalog.csv |
| Ingredient | Ingredient description |
| Qty Per Unit | Quantity of ingredient needed per unit of product |
| Unit | Unit of measure for the ingredient |
| Yield Factor | Yield adjustment factor (e.g., 0.95 = 5% waste) |
| Notes | BOM notes |

---

### PO_Tracker.csv

**46 rows** | Used in: Week 3+

| Column | Description |
|--------|-------------|
| PO Number | Unique purchase order number |
| Supplier ID | Supplier ID from Vendor_Contacts___Terms.csv |
| Supplier Name | Supplier name |
| Ingredient SKU | Ingredient SKU from Ingredient_Catalog.csv |
| Ingredient | Ingredient description |
| Qty Ordered | Quantity ordered |
| Unit | Unit of measure |
| Unit Cost | Cost per unit at time of order |
| Order Date | Date PO was placed |
| Expected Delivery | Expected delivery date |
| Actual Delivery | Actual delivery date (blank if not yet received) |
| Status | PO status (Open, Received, Partial, Cancelled) |

---

### Receiving_Log.csv

**10 rows** | Used in: Week 3+

| Column | Description |
|--------|-------------|
| PO Number | PO Number from PO_Tracker.csv |
| Receipt Date | Date goods were received |
| Ingredient SKU | Ingredient SKU |
| Ingredient | Ingredient description |
| Qty Received | Quantity actually received |
| Qty Ordered | Quantity that was ordered |
| Discrepancy | Difference between ordered and received |
| Quality Notes | Notes on quality or condition at receipt |

---

## Which Files You Need by Week

| Week / Assignment | Files Needed |
|---|---|
| Week 1 | Products___Pricing.csv, Ingredient_Catalog.csv |
| Homework 1 | + Vendor_Contacts___Terms.csv |
| Week 2 | + Sales_Log.csv |
| Homework 2 | + Inventory_Count.csv, Recipes___Ingredients.csv |
| Week 3 | + PO_Tracker.csv, Receiving_Log.csv |

> The `+` means "add to what you already have from prior weeks."
