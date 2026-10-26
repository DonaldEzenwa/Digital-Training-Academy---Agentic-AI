# Contributing to the Agentic AI Field Guide

Thank you for helping improve this learning resource collection. This document explains exactly how to add resources, verify weeks, fix links, and submit changes.

---

## Table of Contents

- [Before You Start](#before-you-start)
- [Getting Started](#getting-started)
- [Adding a New Resource](#adding-a-new-resource)
- [Weekly File Checklist](#weekly-file-checklist)
- [Updating the Roadmap](#updating-the-roadmap)
- [Resource Status Values](#resource-status-values)
- [Quality Rules](#quality-rules)
- [Opening a Pull Request](#opening-a-pull-request)
- [Code of Conduct](#code-of-conduct)

---

## Before You Start

This repository is a curated index, not a course. It links to original source materials (slides, documents, videos, repositories) and keeps personal study notes separate from source content.

Before contributing:

1. **Read the guide.** Open `README.md` at the repo root to understand the 24-week structure.
2. **Pick a week.** Choose a specific week under `agentic-ai-24-week/weeks/week-XX/`.
3. **Check the status.** Open that week's `README.md` to see which resources are recorded and which still need review.
4. **Never claim a resource is reviewed or completed** until you have actually opened and worked through it.

---

## Getting Started

1. **Fork** this repository to your own GitHub account.
2. **Clone** your fork locally:

   ```bash
   git clone https://github.com/<your-username>/Agentic-AI.git
   cd Agentic-AI
   ```

3. **Create a new branch** for your work:

   ```bash
   git checkout -b add-week-03-resources
   ```

4. **Make your changes** (see the sections below).
5. **Commit** with a clear message:

   ```bash
   git commit -m "Add Week 03 slides, readings, and resource notes"
   ```

6. **Push** to your fork:

   ```bash
   git push origin add-week-03-resources
   ```

7. **Open a pull request** against the `main` branch of `Dev0psKing/Agentic-AI`.

---

## Adding a New Resource

For every resource you add to a week's `README.md`, record the following fields:

| Field | What to write |
|-------|---------------|
| **Title** | Use the official name of the resource (slide deck, document, video, repo). |
| **Type** | Slides, reading, video, documentation, repository, or hands-on lab. |
| **Link** | Direct URL to the original source. Do not host copies here. |
| **Review status** | One of: `Not started`, `In progress`, `Completed`, `Reviewed`, `Needs access`. |
| **Last reviewed** | An actual date (YYYY-MM-DD) when you last verified the link. |

Example entry:

```markdown
| Week 03 Foundations deck | Slides | [Open slides](https://docs.google.com/presentation/d/EXAMPLE/edit) | Reviewed | 2026-10-15 |
```

After adding the link, open it and confirm it works. If it requires access you do not have, mark it `Needs access` and note the problem.

---

## Weekly File Checklist

Each week folder (`agentic-ai-24-week/weeks/week-XX/`) should contain:

### `README.md` — Resource Index

- [ ] Official week title (confirmed from source materials)
- [ ] Status line (links recorded / verified / pending)
- [ ] Resource index table with: Resource, Type, Link, Review status, Last reviewed
- [ ] Learning objectives (filled in after reviewing sources, not inferred)
- [ ] Suggested workflow checklist
- [ ] Links to `resource-notes.md` and `learning-log.md`

### `resource-notes.md` — Personal Notes

- [ ] Official topic
- [ ] Key concepts (added after review)
- [ ] Notes by resource (link, purpose, useful takeaways, questions)
- [ ] My summary (written in your own words)

### `learning-log.md` — Dated Log

- [ ] Date started
- [ ] Date completed (when finished)
- [ ] Status (Not started / In progress / Completed)
- [ ] What I learned
- [ ] What I practiced
- [ ] Questions to revisit
- [ ] Deliverable / evidence (notebook, code, screenshot, project — no confidential materials)
- [ ] Next steps

---

## Updating the Roadmap

The 24-week tracking roadmap lives at `agentic-ai-24-week/ROADMAP.md`. Update it only when:

- A week's official topic or learning objectives are confirmed from source materials.
- A week's status changes (for example, from "Links recorded" to "Verified").
- Resources are added or removed for a week.

Edit the weekly progress table:

| Week | Topic | Status |
|------|-------|--------|
| 03 | Agentic foundations | Verified |

Do not invent topics or outcomes. If the official materials have not been reviewed yet, leave the topic as "To verify from source materials."

---

## Resource Status Values

Use exactly these values in review status columns:

- `Not started` — not reviewed yet
- `In progress` - currently studying
- `Completed` - worked through the material
- `Reviewed` - link and description checked
- `Needs access` - source cannot currently be opened

Always pair a status change with a `Last reviewed` date so others know when it was verified.

---

## Quality Rules

1. **Link to original sources.** Do not copy slides, documents, or course materials into this repository without explicit permission. Link to the original instead.
2. **Separate source material from personal notes.** Keep copied or quoted source content clearly distinct from your own summaries and reflections.
3. **Explain why a resource matters.** After reviewing, add a short explanation in your own words about what it teaches and why it is useful.
4. **Check links periodically.** Verify links still work and record the `Last reviewed` date.
5. **Do not claim completion early.** Never mark a resource as completed or reviewed until you have actually opened and studied it.
6. **Respect copyright and privacy.** Never upload private, confidential, or restricted course materials. Do not republish restricted content.
7. **Use real dates.** `Last reviewed` must be an actual calendar date, not a placeholder.

---

## Opening a Pull Request

1. Push your branch to your fork.
2. Open a pull request from your branch to `Dev0psKing/Agentic-AI:main`.
3. In the pull request description, include:
   - Which week(s) you worked on.
   - What resources you added, verified, or fixed.
   - Whether you updated `ROADMAP.md`.
   - Any links that still need access.
4. Keep the PR focused on one topic (one week or one type of fix) where possible.
5. Respond to review comments and update your branch as requested.

---

## Code of Conduct

This project follows the Contributor Covenant Code of Conduct. Be respectful and constructive in suggestions, report broken or permission-restricted links, and assume good faith in others' contributions.

---

## Questions

If you are unsure whether something belongs in this repository, open an issue describing what you want to add before submitting a pull request.
