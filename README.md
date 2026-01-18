# uv-ml-collab-starter

A collaborative **machine learning starter repository** designed to practice:

- `uv`-based environment and dependency management
- Modern Python project structure
- Clean Git workflows (branching, PRs, code review)
- A simple end-to-end ML pipeline (data → analysis → modeling)

This repository is intentionally structured as a **teaching and collaboration sandbox**, not a finished product.

---

## 🎯 Purpose of This Repository

This repo is designed to simulate a **real-world collaborative workflow** while keeping the technical scope approachable.

Key goals:

- Learn how to work with `uv` in a realistic project
- Practice cloning, branching, and pull requests
- Understand how unfinished “main” branches are used as starting points
- Build confidence contributing to shared codebases

---

## 🌳 Branching Philosophy (Very Important)

### `main` branch

- **Always unfinished**
- **Never merged into**
- Serves as a **clean starting template** for all students
- Safe to clone at any time

> Think of `main` as a permanent “starter kit,” not a production branch.

---

### `dev` branch

- Integration branch for student work
- Pull requests are made **into `dev` only**
- Used for review, discussion, and learning

---

### Student branches (example)

Each student creates their **own branch**, for example:

`dev-denis`
`dev-alex`
`dev-sam`

These branches are where all development happens.

---

## 🚫 Hard Rule

**Pull requests are NEVER made to `main`.**

- ❌ No PRs to `main`
- ✅ PRs only go **from student branch → `dev`**

This rule exists to:

- Protect the starter template
- Mirror professional Git workflows
- Avoid accidental overwrites or confusion

The `main` branch exists only as a clean, immutable starting point.

---

## 🧑‍💻 Recommended Workflow (Step-by-Step)

### 1️⃣ Clone the repository (from `main`)

```bash
git clone git@github.com:<your-org>/uv-ml-collab-starter.git
cd uv-ml-collab-starter
```

### 2️⃣ Create your own branch from `main`

All student work begins from the `main` branch.  You do not need to switch branches before creating your own — your branch should be created directly from `main`.

```bash
git switch -c dev-<your-name>
```

Example:

```bash
git switch -c dev-denis
```

### 3️⃣ Set up the environment using uv

```bash
uv sync
source .venv/bin/activate
```

Advanced users can try installing the development tools as well.

Note: `--group dev` **adds** development tools on top of the base dependencies — it does not replace `uv sync`.

```bash
uv sync
uv sync --group dev  
source .venv/bin/activate
```

_**What does `--group dev` do?**_

It installs the optional **development dependency group**, which includes tools such as testing and code formatting utilities.

In this project, using `--group dev` is optional and mainly for practice.  
Skipping it will still allow you to run notebooks and core ML code.

You can always run `uv sync --group dev` later if you want the additional tools.

### 4️⃣ Do your work

See the student README for guidance on the problem statement.  It can be found here:
`docs/00_overview/student-README.md`

Examples (this repo uses a `/scripts` directory for runnable tasks):

- Run data from `scripts/download_data.py` into `data/raw/`
- Explore data in notebooks/
- Add training logic in src/
- Experiment, break things, fix them — that’s the point

Note: The `src/` directory is included to expose students to standard Python project structure.  
Most hands-on work in this repo intentionally uses the `scripts/` directory.

### 5️⃣ Commit your changes

```bash
git add .
git commit -m "Add initial data download and exploration"
```

### 6️⃣ Push your branch to GitHub

```bash
git push origin dev-<your-name>
```

### 7️⃣ Open a Pull Request to `dev`

- Go to the GitHub repo page
- Click “Compare & pull request”
- Ensure the base branch is `dev` and the compare branch is your branch
- Add a descriptive title and summary of your changes
- Request reviews from peers or instructors
- Submit the PR

---

## 🧠 What This Repo Is (and Is Not)

### ✅ This repo IS

- A **learning environment** for practicing modern Python workflows
- A **collaboration sandbox** for working with branches and pull requests
- A place to practice **`uv`-based environment and dependency management**
- A realistic simulation of how unfinished starter templates are used
- A **safe space to experiment**, break things, and learn through review

---

### ❌ This repo is NOT

- A production-ready machine learning system
- A completed or polished project
- A place to merge work directly into `main`
- A shortcut around Git rules “just this once”
- A personal sandbox detached from collaboration norms

---

## 📌 Final Notes

- Keep commits **small, focused, and descriptive**
- Use pull request descriptions to explain:
  - What you worked on
  - What questions you have
  - Where you want feedback
- Do not worry about being “wrong” — learning happens during review
- Respect the branching rules; they exist to mirror real-world team workflows

If this process feels stricter than expected — that’s intentional.  
This is how professional teams collaborate every day.

Happy building 🚀
