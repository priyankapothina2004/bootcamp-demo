# How to Add Your Page — Step-by-Step Guide

Welcome! Follow these steps to add your own profile page to the bootcamp showcase.
This guide is written for beginners, so every step is explained in detail.

---

## What You Will Need

- A [GitHub account](https://github.com) (free)
- [Git](https://git-scm.com/downloads) installed on your computer
- A text editor (e.g. [VS Code](https://code.visualstudio.com/))

---

## Step 1 — Fork this Repository

A **fork** is your own personal copy of this project on GitHub.

1. Go to the top of this repository's GitHub page.
2. Click the **Fork** button (top-right corner).
3. GitHub will create a copy of the repo under your account.

---

## Step 2 — Clone Your Fork to Your Computer

**Cloning** downloads your fork so you can edit files locally.

1. On your forked repo page, click the green **Code** button.
2. Copy the URL shown (it will look like `https://github.com/YOUR-USERNAME/bootcamp-demo.git`).
3. Open a terminal (Command Prompt, Git Bash, or Terminal) and run:

```bash
git clone https://github.com/YOUR-USERNAME/bootcamp-demo.git
```

4. Move into the project folder:

```bash
cd bootcamp-demo
```

---

## Step 3 — Copy the TEMPLATE Folder and Rename It

The `TEMPLATE` folder contains a ready-made `index.html` for you to fill in.

1. Copy the entire `TEMPLATE` folder.
2. Rename the copy to `participant-yourname` — replace `yourname` with your actual first name or GitHub username.

**On Mac / Linux:**

```bash
cp -r TEMPLATE participant-yourname
```

**On Windows (Command Prompt):**

```cmd
xcopy TEMPLATE participant-yourname\ /E /I
```

> Example: if your name is Priya, the folder should be called `participant-priya`.

---

## Step 4 — Edit Your index.html

1. Open `participant-yourname/index.html` in your text editor.
2. Replace all the placeholder text with your real information:
   - `Your Name` → your name
   - `Your project description` → what you built
   - `your-github-username` → your GitHub username
   - etc.
3. Look for the `✏️` comments in the file — they mark every spot you need to update.
4. Save the file when you are done.

---

## Step 5 — Commit and Push Your Changes

Now you will save your changes to Git and upload them to GitHub.

```bash
# Stage your new folder
git add participant-yourname/

# Create a commit with a clear message
git commit -m "Add participant-yourname"

# Push to your fork on GitHub
git push origin main
```

> Replace `yourname` with the name you used for your folder.

---

## Step 6 — Create a Pull Request

A **pull request** (PR) asks the maintainers to add your changes to the main project.

1. Go to your forked repo on GitHub.
2. You should see a banner saying **"Compare & pull request"** — click it.
   - If you don't see it, click the **Pull requests** tab, then **New pull request**.
3. Make sure:
   - **base repository** is the original `bootcamp-demo` repo
   - **head repository** is your fork
4. Give your PR a short title, e.g. `Add participant-priya`.
5. Click **Create pull request**.

That's it! A maintainer will review your PR and merge it. Once merged, the registry is updated automatically and your page will appear in the showcase.

---

## Need Help?

If you get stuck at any step, open an **Issue** on this repository and describe what went wrong. We're happy to help!
