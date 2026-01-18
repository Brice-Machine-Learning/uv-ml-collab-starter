# 🧠 Machine Learning Project — Census Income Prediction

Welcome to this collaborative machine learning project.

Your goal is to work through a **realistic, end-to-end ML workflow** using a public dataset, modern Python tooling, and professional Git practices.

This project is intentionally *not* pre-polished. Real-world data is messy — learning how to deal with that mess is the point.

---

## 📊 Dataset Overview

We are using the **UCI Adult (Census Income) dataset**, which contains demographic and employment-related attributes collected from U.S. Census data.

Each row represents **one individual**.

The dataset is provided in its **raw, unmodified form** and is downloaded into:

```text
data/raw/adult/adult.data
```

Do **not** edit this file directly.

---

## 🎯 Problem Statement

> **Given a set of demographic and employment features for an individual, predict whether their annual income exceeds $50,000.**

This is a **binary classification problem**.

---

## 🧠 What You Are Predicting

### Target variable

* **Income level**

  * `<=50K`
  * `>50K`

Your model should learn patterns in the input data that help distinguish between these two outcomes.

---

## 🧮 Type of Machine Learning Task

| Aspect        | Description                       |
| ------------- | --------------------------------- |
| Learning type | Supervised learning               |
| Task          | Binary classification             |
| Input         | Demographic & employment features |
| Output        | Income class (`>50K` or `<=50K`)  |

---

## 📥 Input Features (Conceptual)

The raw dataset does **not** include column headers, but the fields correspond to attributes such as:

* Age
* Work class
* Education level
* Occupation
* Marital status
* Hours worked per week
* Capital gains / losses
* Sex, race, and native country

Part of the exercise is to **interpret and assign meaningful column names** when loading the data.

---

## ⚠️ Important Notes About the Data

This dataset is intentionally **messy**, just like real-world data:

* Missing values are represented by `?`
* Many fields contain inconsistent whitespace
* Categorical and numeric values are mixed
* No header row is provided
* File extension is `.data`, not `.csv`

This is normal — and expected.

---

## 📁 Project Structure (What to Use)

* **`scripts/`**

  * Contains runnable scripts (e.g., downloading data)
  * This is where most hands-on work begins

* **`data/raw/`**

  * Stores immutable raw data
  * Never modify files here

* **`data/processed/`**

  * Where cleaned or transformed datasets should be written

* **`src/`**

  * Included to expose you to standard Python project structure
  * Some logic may move here later

* **`notebooks/`**

  * Use for exploration, visualization, and experimentation

---

## 🧪 Suggested Modeling Approach (High-Level)

You are **not** expected to build a perfect model.

A reasonable first goal is:

1. Load and inspect the raw data
2. Handle missing values and whitespace
3. Encode categorical features
4. Split data into training and test sets
5. Train a simple classification model
6. Evaluate performance on unseen data

Focus on **clarity and reasoning**, not complexity.

---

## 🧑‍💻 Collaboration Expectations

* Create your own branch from `main` (e.g., `dev-yourname`)
* Commit small, focused changes
* Open pull requests **to `dev` only**
* Use PR descriptions to explain:

  * What you did
  * What questions you have
  * Where you’d like feedback

This repo is a **learning environment** — mistakes are expected.

---

## 🚫 What This Project Is Not

* Not a production system
* Not a Kaggle-style leaderboard competition
* Not about squeezing out maximum accuracy
* Not about copying pre-built solutions

This project is about learning **process**, not just results.

---

## ✅ Success Criteria

You are successful if you can:

* Explain how the data was cleaned
* Justify modeling decisions
* Interpret evaluation results
* Collaborate cleanly using Git and pull requests

---

## 📌 Final Reminder

Real-world ML is messy, iterative, and collaborative.

Take your time, ask questions, and treat this as practice for how real teams actually work.

Happy modeling 🚀
