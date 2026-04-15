# SCM 478 Grading

## Assessment Framework

| Assessment | Weight | What It Measures |
|---|---|---|
| Module Builds (8) | 15% | Does the app work? Is it deployed? |
| Homework (10) | 15% | Practice and preparation between scenarios. |
| Transfer Exams (4) | 30% | Can you apply skills to a new company? Spec brief + app + walkthrough. |
| Mega Exam | 30% | Integrated system: correct, connected, documented. Different company. |
| Oral Demonstration | 10% | Can you explain and defend your system live? |

## Module Builds (15%)

Module Builds are pass/fail. Your app either meets the requirements or it doesn't.

**How they're graded:** Your app includes a Self-Check page that runs automated validation checks. Each check has a point value. Your Self-Check score is the primary grade input, subject to visual verification by the instructor (filters work, charts display, metrics show correct values).

- **100% on Self-Check + app works visually = Complete**
- **Anything less = Incomplete -- resubmit**

You can resubmit Module Builds until they pass.

## Homework (15%)

Homework assignments extend the Peak Fuel app with new features that Maria needs. Each homework is framed as Maria's operational question -- you figure out what data and calculations answer her question, then use AI to build it.

Homework is graded on the same Self-Check system as Module Builds. Some homeworks have additional requirements (explanations, recommendations) that are evaluated by the instructor.

## Transfer Exams (30%)

Transfer Exams present a **different company** with different data. You must apply the skills you built with Peak Fuel to a novel context. You cannot copy-paste your Peak Fuel code -- you must understand the SCM concepts well enough to rebuild them for a new scenario.

Each Transfer Exam has three components:
1. **Specification Brief (1-2 pages):** Written document describing the system design -- inputs, outputs, calculations, and downstream connections. No code.
2. **Deployed Streamlit App:** A working application meeting the exam requirements.
3. **Walkthrough (2-3 minutes):** In the following class, you walk the instructor through your app and explain your design decisions.

## Mega Exam (30%)

The Mega Exam is the capstone. It uses Kunzler's cafe data -- a completely different company from Peak Fuel. You build an integrated system with four connected modules: forecasting, planning, inventory, and purchasing.

Submitted as: deployed app + GitHub repo + architecture document (3-5 pages).

## Oral Demonstration (10%)

A 5-7 minute live demo of your Mega Exam app, followed by 2-3 minutes of questions from the instructor. You must explain how your modules connect, what calculations they perform, and why you made specific design decisions.

## Self-Check System

Every app you build includes a Self-Check page that validates your work against the assignment requirements. The Self-Check:

- Shows green (pass) or red (fail) for each requirement
- Displays the point value of each check
- Tells you what's wrong but not how to fix it
- Only shows checks for the assignment you select from a dropdown

**Use it constantly.** After every change: commit, wait for redeploy, click Self-Check. Fix one issue at a time. Your goal is always 100% before submitting.

See [setup/self-check-setup.md](setup/self-check-setup.md) for installation instructions.

## Late Policy

Module Builds and Homework can be resubmitted until the end of the unit with no penalty. Transfer Exams are due on the assigned date. The Mega Exam and Oral Demonstration are due in Week 13.

## Grade Scale

| Grade | Percentage |
|---|---|
| A | 93-100% |
| A- | 90-92% |
| B+ | 87-89% |
| B | 83-86% |
| B- | 80-82% |
| C+ | 77-79% |
| C | 73-76% |
| C- | 70-72% |
| D | 60-69% |
| F | Below 60% |
