# Week 1 Tutorial: Setting Up Your Development Stack

**SCM 478 — Operations Analysis and Modeling**  
Complete this tutorial before Day 2 of class.

---

## What You're Building This Semester

This semester you will build a supply chain management system for Peak Fuel Foods — a small food company that makes protein burritos, bowls, wraps, bars, and smoothie packs. By Week 13, you'll have a working web application that helps the founder, Maria Solano, answer her most important operational questions: What do I need to produce this week? Do I have enough ingredients? What do I need to order, and from whom?

You don't need to know how to code. You'll use AI to help you write the code, and you'll use three free tools to store, run, and share your application:

- **GitHub** — where your code lives (like Google Drive for code)
- **Streamlit** — turns your code into a web app anyone can visit
- **AI (Claude, ChatGPT, etc.)** — your coding partner

Today's goal: create accounts on GitHub and Streamlit, and deploy a simple app so you can see the full cycle working.

---

## Step 1: Create Your GitHub Account

1. Go to [github.com](https://github.com)
2. Click **Sign up**
3. Enter your email, create a password, and choose a username
   - **Use a professional username** — employers will see this. Your name or a variation of it works well (e.g., `jsolano`, `maria-solano-scm`). Avoid `xXx_gamer_xXx`.
4. Complete the verification and click **Create account**
5. Check your email and verify your account

You now have a GitHub account.

---

## Step 2: Create Your First Repository

A repository ("repo") is a project folder on GitHub. Your app will live here.

1. On GitHub, click the **+** icon in the top right, then **New repository**
2. Name it: `scm478-peak-fuel` (or similar — lowercase, no spaces)
3. Set it to **Public** (Streamlit Cloud needs to see it)
4. Check **Add a README file**
5. Click **Create repository**

You now have an empty project.

---

## Step 3: Add Your First Two Files

You need two files to make a Streamlit app work: `requirements.txt` (tells Streamlit what software to install) and `app.py` (your actual app).

### File 1: requirements.txt

1. In your repo, click **Add file** → **Create new file**
2. Name it exactly: `requirements.txt`
3. Paste this content:

```
streamlit
pandas
plotly
```

4. Click **Commit changes** (green button at bottom)

### File 2: app.py

1. Click **Add file** → **Create new file** again
2. Name it exactly: `app.py`
3. Paste this content:

```python
import streamlit as st

st.set_page_config(page_title="Peak Fuel Foods", page_icon="⚡", layout="wide")

st.title("⚡ Peak Fuel Foods")
st.subheader("Supply Chain Management System")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Ingredients", "Sales", "Purchasing"])

if page == "Dashboard":
    st.write("Welcome to Peak Fuel Foods! This system will help Maria manage her supply chain.")
    st.write("Use the sidebar to navigate between modules.")
elif page == "Ingredients":
    st.write("Ingredient catalog will go here.")
elif page == "Sales":
    st.write("Sales and demand data will go here.")
elif page == "Purchasing":
    st.write("Purchase orders and supplier info will go here.")

st.sidebar.divider()
st.sidebar.caption("SCM 478 • BYU-Idaho")
```

4. Click **Commit changes**

Your repo now has three files: README.md, requirements.txt, and app.py.

---

## Step 4: Connect to Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **Sign up** or **Continue with GitHub**
3. Authorize Streamlit to access your GitHub account
4. Click **New app**
5. Select your repository (`scm478-peak-fuel`)
6. Main file path: `app.py`
7. Click **Deploy**

Wait 1–2 minutes. Streamlit is installing your requirements and starting your app.

When it's done, you'll see your app live at a URL like:  
`https://your-username-scm478-peak-fuel-app-xxxxx.streamlit.app`

**Bookmark this URL.** This is your app. You'll submit this URL for assignments throughout the semester.

---

## Step 5: Verify It Works

Open your app URL in a browser. You should see:
- A title: "⚡ Peak Fuel Foods"
- A subtitle: "Supply Chain Management System"
- A sidebar with four navigation options
- Placeholder text on each page

If you see this, congratulations — you just deployed a web application with zero prior coding experience. Share the URL with a friend or family member if you want to show off.

---

## Step 6: Test the Edit-Deploy Cycle

This is the most important thing to understand: when you change a file on GitHub, Streamlit automatically updates your app.

1. Go back to your GitHub repo
2. Click on `app.py`
3. Click the pencil icon (✏️) to edit
4. Find the line that says `st.write("Welcome to Peak Fuel Foods!")` and change it to `st.write("Welcome to Peak Fuel Foods! Built by [YOUR NAME].")`
5. Click **Commit changes**
6. Go back to your Streamlit app and refresh the page (it may take 30–60 seconds to update)

You should see your name in the welcome message. That's the full cycle: **edit on GitHub → commit → app updates automatically**. You'll use this cycle hundreds of times this semester.

---

## Troubleshooting

**App won't deploy:**
- Make sure `app.py` is in the root of your repo, not inside a folder
- Make sure `requirements.txt` is spelled correctly (not `requirement.txt`)
- Check that your repo is Public, not Private

**"No module named streamlit" error:**
- Your `requirements.txt` is missing or misspelled. Open it and make sure it contains the word `streamlit`

**GitHub account not found by Streamlit:**
- Verify your email on GitHub (check your inbox for a verification email)
- Try signing out of Streamlit and signing back in with GitHub

**App shows "Please wait..." forever:**
- Streamlit Cloud sometimes takes 2–3 minutes for the first deploy. Be patient.
- If it's been more than 5 minutes, click "Manage app" in the bottom-right corner and check the logs for error messages

---

## What's Next

In class on Day 2, we'll load Peak Fuel's data into your app and build the first real feature: an ingredient catalog viewer with filters. Bring your laptop and have your GitHub repo and Streamlit app ready to go.

Before Day 2, also make sure you've read:
- **Maria Solano's Founder's Story** — the scenario for the entire semester
- **Mapping Business Operations to Data** — the conceptual foundation for what we're building
