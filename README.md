# Git & GitHub Bootcamp — KIET Group of Institutions

Welcome! This repository is the hands-on exercise for the **Git & GitHub Bootcamp** at KIET Group of Institutions. If you are here, you are about to make your very first open-source-style contribution. Don't worry — every step is explained, and mistakes are totally okay. That's what the bootcamp is for!

---

## What Is This Exercise About?

Each team will build a small **participant showcase** — a collection of profile pages, one per team member, all living in the same repository. By the end of the session you will have practised the core Git & GitHub workflow that real software teams use every day:

```
Fork → Clone → Edit → Commit → Push → Pull Request
```

---

## Team Structure

Teams are made up of **5 members**:

| Role | Responsibility |
|---|---|
| **Team Lead (1 person)** | Creates the repository, sets up the base project, reviews Pull Requests, and runs `update.py` to refresh the main page |
| **Contributors (4 people)** | Fork the repo, add their own profile folder, and open a Pull Request |

---

## Demo Flow

Here is the sequence of events during the bootcamp session:

1. **Team Lead** creates a new GitHub repository and pushes the starter code.
2. **Team Lead** shares the repository link with the rest of the team.
3. Each **Contributor** forks the repository to their own GitHub account.
4. Each **Contributor** clones their fork, creates their folder (`rollno-name/`), fills in `info.json` and writes their own `index.html`, then commits their changes.
5. Each **Contributor** pushes their changes and opens a **Pull Request** back to the Team Lead's repository.
6. **Team Lead** reviews and merges each Pull Request.
7. The main `index.html` is updated automatically (GitHub Actions runs `update.py` on every merge).
8. The finished showcase — with everyone's profile card — is visible on the live site!

---

## How to Participate

Ready to add your page? All the instructions are in **[CONTRIBUTING.md](CONTRIBUTING.md)**.

It will walk you through every step:
- Forking and cloning the repo
- Creating your folder and filling in `info.json`
- Writing your own `index.html` profile page
- Committing and pushing your changes
- Opening a Pull Request

> First time using Git? No problem. The guide is written for absolute beginners and explains each command as you go.

---

## Project Structure

```
bootcamp-demo/
├── index.html              # Main showcase page (updated by update.py)
├── update.py               # Script that reads all info.json files and updates index.html
├── TEMPLATE/               # Copy this folder to create your own page
│   ├── index.html          # Starter template — replace with your own content
│   └── info.json           # Fill in your roll number, name, and photo URL
├── participants/
│   └── rollno-name/        # Your folder, named as your roll number + your name
│       ├── index.html      # Your profile page (you write this)
│       └── info.json       # Your roll number, name, and photo URL
├── CONTRIBUTING.md         # Step-by-step guide for contributors
└── README.md               # You are here!
```

---

## Need Help?

- Read through [CONTRIBUTING.md](CONTRIBUTING.md) carefully — it covers the most common questions.
- If you are still stuck, open an **Issue** on this repository and describe what went wrong. No question is too basic!
- Ask your Team Lead or the bootcamp instructor.

---

*Happy committing! You've got this.*
