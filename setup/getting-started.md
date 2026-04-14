# Getting Started

This guide walks you through the one-time setup required for SCM 478. Complete all steps before the first day of class.

---

## Step 1: Install Python

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download Python **3.10 or later**
2. Run the installer. On Windows, check **"Add Python to PATH"** before clicking Install
3. Verify the install: open a terminal and run:
   ```
   python --version
   ```
   You should see something like `Python 3.11.x`

---

## Step 2: Install VS Code

1. Download VS Code from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install the **Python extension** (search "Python" in the Extensions sidebar, install the one from Microsoft)
3. Recommended: also install the **Pylance** extension for better code suggestions

---

## Step 3: Create a GitHub Account

1. Go to [github.com](https://github.com) and create a free account if you do not already have one
2. Use a professional username — this account will be part of your portfolio

---

## Step 4: Install Git

1. Download Git from [git-scm.com](https://git-scm.com/)
2. During installation, accept all defaults
3. Verify: open a terminal and run:
   ```
   git --version
   ```

---

## Step 5: Clone the Course Repository

1. Open a terminal
2. Navigate to the folder where you want to store your coursework
3. Run:
   ```
   git clone https://github.com/[instructor-will-provide-url]/scm478-course.git
   ```
4. Open the cloned folder in VS Code

---

## Step 6: Set Up a Virtual Environment

Inside the cloned folder, run:

```bash
python -m venv .venv
```

Activate it:
- **Windows:** `.venv\Scripts\activate`
- **Mac/Linux:** `source .venv/bin/activate`

Install required packages:

```bash
pip install streamlit pandas matplotlib
```

---

## Step 7: Run the Self-Check

```bash
python setup/self_check.py
```

See [self-check-setup.md](self-check-setup.md) for what the output should look like. If anything fails, check the troubleshooting section there before asking for help.

---

## Troubleshooting

**Python not found after install:** Restart your terminal. If still missing, verify "Add Python to PATH" was checked during install.

**`pip install` fails:** Make sure your virtual environment is activated (you should see `(.venv)` in your prompt).

**VS Code doesn't recognize the virtual environment:** Open the command palette (`Ctrl+Shift+P`), search "Python: Select Interpreter", and choose the one in `.venv`.
