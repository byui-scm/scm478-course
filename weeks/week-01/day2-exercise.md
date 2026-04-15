# Week 1, Day 2: Building the Ingredient Catalog Viewer

**SCM 478 — In-Class Exercise**  
**Scaffolding Level: Heavy** — follow along step by step.

---

## Setup Check (5 minutes)

Before we start building, verify:

- [ ] GitHub account with a repo for this course
- [ ] Deployed Streamlit app visible at your URL
- [ ] Two CSV files downloaded: [Products___Pricing.csv](https://git-link.vercel.app/api/download?url=https%3A%2F%2Fgithub.com%2Fbyui-scm%2Fscm478-course%2Fblob%2Fmain%2Fdata%2F&filename=Products___Pricing.csv) and [Ingredient_Catalog.csv](https://git-link.vercel.app/api/download?url=https%3A%2F%2Fgithub.com%2Fbyui-scm%2Fscm478-course%2Fblob%2Fmain%2Fdata%2F&filename=Ingredient_Catalog.csv)

If anything isn't working, raise your hand now.

---

## Upload the Data Files to GitHub (5 minutes)

1. Go to your GitHub repo
2. Click **Add file** → **Upload files**
3. Drag both CSV files into the upload area
4. Click **Commit changes**

Your repo should now have: `app.py`, `requirements.txt`, `README.md`, and the two CSV files.

---

## Build the Ingredient Catalog Viewer (20 minutes)

### Step 1: Open your AI tool

Open Claude (claude.ai) or ChatGPT in a separate tab.

### Step 2: Give it this prompt

Copy and paste this exactly:

> I have a Streamlit app with two CSV files in the same directory:
>
> 1. `Products___Pricing.csv` with columns: SKU, Product Name, Description, Category, Unit of Measure, Retail Price
>
> 2. `Ingredient_Catalog.csv` with columns: Ingredient SKU, Description, Order Unit, Cost Per Unit, MOQ, Primary Supplier ID, Primary Supplier Name
>
> Please write an app.py that does the following:
>
> - Load both CSV files using pandas
> - Create a sidebar with navigation (Dashboard, Ingredients, Sales, Purchasing)
> - On the "Ingredients" page:
>   - Show a title "Ingredient Catalog"
>   - Add a dropdown filter for "Primary Supplier Name" (with an "All" option)
>   - Display the filtered ingredient table
>   - Show three metric cards above the table: total number of ingredients, number of unique suppliers, and average cost per unit
> - On the "Dashboard" page, show the list of products from Products___Pricing.csv as a simple table
> - Keep the other pages as placeholders
> - Use st.set_page_config with page_title="Peak Fuel Foods", page_icon="⚡", layout="wide"

### Step 3: Read the AI's response

Before pasting, scan the code for:
- Does it load both CSV files? (Look for `pd.read_csv`)
- Does it create a dropdown? (Look for `st.selectbox`)
- Does it show metrics? (Look for `st.metric`)
- Does it display a table? (Look for `st.dataframe`)

### Step 4: Replace your app.py on GitHub

1. Click on `app.py` in your repo
2. Click the pencil icon to edit
3. Select all existing content and delete it
4. Paste the new code from AI
5. Click **Commit changes**

### Step 5: Check your app

1. Go to your Streamlit URL
2. Wait 30-60 seconds for redeploy
3. Click "Ingredients" in the sidebar
4. You should see metric cards, a supplier filter, and a data table

**Common errors:**
- **File not found**: CSV filenames in code don't match actual filenames. Check spaces, underscores, capitalization.
- **Column not found**: Column names don't match CSV headers. Open the CSV and check exact names.
- **Import error**: Make sure `pandas` is in your `requirements.txt`

---

## Explore and Extend (15 minutes)

Pick one extension and write your own AI prompt this time:

**Option A:** Add a second filter by "Order Unit" (Each, Package, Gallon, etc.)

**Option B:** Add a bar chart showing number of ingredients per supplier

**Option C:** Highlight ingredients where Cost Per Unit exceeds $10.00

Describe what you want in plain English, paste the result, commit, and check.

---

## What You Just Learned

1. **AI as a development tool.** You described what you wanted, AI wrote code, you deployed it. That's the workflow for the entire semester.

2. **Master data visibility.** Maria's 33 ingredients — costs, MOQs, suppliers — are now visible and filterable in a web app. This is the foundation of every supply chain system.

The question to carry forward: *What else would Maria need to see?*
