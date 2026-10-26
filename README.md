# Agentic AI Field Guide

**Learner:** Donald Ezenwa

## Table of Contents

- [About This Guide](#about-this-guide)
- [The 24-Week Journey](#the-24-week-journey)
- [How to Use This Guide](#how-to-use-this-guide)
- [Weekly Resources](#weekly-resources)
- [Resource Status Key](#resource-status-key)
- [Curation Principles](#curation-principles)
- [Repository Structure](#repository-structure)
- [How to Contribute](#how-to-contribute)

---

## About This Guide

The **Agentic AI Field Guide** is a 24-week learning journey that collects, organizes, and tracks the resources, hands-on exercises, and personal study notes behind an agentic artificial intelligence training program.

This repository is not a course itself. It is a field guide - a living index that points to the original source materials (slides, documents, videos, repositories) and keeps a personal record of what was learned, what was practiced, and what still needs clarification.

It exists to answer one question for every week of the program:

> *"What resources do I need, where are they, and what did I get out of them?"*

If you are stepping into this program for the first time, start at [Week 01](agentic-ai-24-week/weeks/week-01/README.md) and work your way forward. If you are a contributor or reviewer, see [How to Contribute](#how-to-contribute).

---

## The 24-Week Journey

The guide is organized into 24 weeks, each with its own folder under `agentic-ai-24-week/weeks/`. Each planned week contains a resource index and notes file:

| File | Purpose |
|------|---------|
| `README.md` | Resource index - links to the week's slides, documents, and repositories, plus review status |
| `resource-notes.md` | Personal notes on what each resource covers, key takeaways, and open questions |

### Current progress

| Week | Status | Resource index |
|------|--------|----------------|
| [Week 01](agentic-ai-24-week/weeks/week-01/README.md) | Links recorded; content not yet verified | [View resources](agentic-ai-24-week/weeks/week-01/README.md) |
| [Week 02](agentic-ai-24-week/weeks/week-02/README.md) | Links recorded; content not yet verified | [View resources](agentic-ai-24-week/weeks/week-02/README.md) |
| [Week 03](agentic-ai-24-week/weeks/week-03/README.md) | Python Fundamentals resources verified | [View resources](agentic-ai-24-week/weeks/week-03/README.md) |
| [Week 04](agentic-ai-24-week/weeks/week-04/README.md) | Python OOP and File Handling links recorded | [View resources](agentic-ai-24-week/weeks/week-04/README.md) |
| Weeks 05–24 | Templates awaiting source materials | Reserved for future resources |

Weeks 01 through 04 have source links recorded, but their full contents and learning outcomes remain to be verified against the source materials. Weeks 05 through 24 contain reusable templates awaiting their official curriculum.

The full tracking roadmap lives at [agentic-ai-24-week/ROADMAP.md](agentic-ai-24-week/ROADMAP.md).

---

## How to Use This Guide

Whether you are a learner, a reviewer, or a contributor, follow these steps:

1. **Open the relevant week** in `agentic-ai-24-week/weeks/`.
2. **Start with that week's `README.md`** - it lists the official source materials and their review status.
3. **Open the linked source materials** - slides, documents, videos, or repositories. Always prefer the original source.
4. **Complete the hands-on activity** - each week includes practical exercises or deliverables to work through.
5. **Record your own notes** - write what you learned in `resource-notes.md` and add practice evidence when the week's materials are available.
6. **Update the checklist and status** - mark items complete and update the roadmap when you finish a week.

Never claim a resource is completed or reviewed until you have actually opened and worked through it.

---

## Weekly Resources

Each week's `README.md` contains a resource index table with four columns:

| Column | What it means |
|--------|---------------|
| **Resource** | The name or description of the material |
| **Type** | Slides, reading, video, documentation, repository, or hands-on lab |
| **Link** | Direct URL to the original source |
| **Review status** | Whether the content has been checked yet |

Use the [Resource Status Key](#resource-status-key) to understand what each status label means.

---

## Resource Status Key

| Status | Meaning |
|--------|---------|
| `Not started` | The resource has not been reviewed yet |
| `In progress` | The resource is currently being studied |
| `Completed` | The material has been worked through in full |
| `Reviewed` | The link and description have been checked |
| `Needs access` | The source cannot currently be opened (permissions, broken link, etc.) |

---

## Curation Principles

To keep this guide trustworthy and useful, every contribution should follow these rules:

1. **Link to original sources.** Do not copy course materials, slides, or documents into this repository without explicit permission. Link to the original instead.
2. **Separate source material from personal notes.** Keep copied or quoted source content clearly distinct from your own summaries and reflections.
3. **Explain why a resource matters.** After reviewing a resource, add a short explanation in your own words about what it teaches and why it is useful.
4. **Check links periodically.** Verify that links still work and record the date they were last reviewed.
5. **Do not claim completion early.** Do not mark a resource as completed or reviewed until you have actually opened and studied it.
6. **Respect copyright and privacy.** Never upload private, confidential, or restricted course materials.

---

## Repository Structure

```text
.
├── README.md                              # This file - the field guide overview
├── agentic-ai-24-week/                    # The 24-week program scaffold
│   ├── README.md                          # Week-by-week program overview
│   ├── ROADMAP.md                         # 24-week tracking roadmap
│   └── weeks/
│       ├── week-01/
│       │   ├── README.md                  # Week 1 resource index
│       │   ├── resource-notes.md          # Week 1 personal notes
│       │   └── resource-notes.md          # Week 1 personal notes
│       ├── week-02/
│       │   ├── README.md                  # Week 2 resource index
│       │   ├── resource-notes.md          # Week 2 personal notes
│       │   └── resource-notes.md          # Week 2 personal notes
│       ├── week-03/
│       │   ├── README.md                  # Week 3 resource index
│       │   ├── resource-notes.md          # Week 3 personal notes
│       │   └── resources/                 # Python Fundamentals materials
│       └── week-04/ through week-24/      # Future-week templates
```

Weeks 04 through 24 use the same lightweight README and resource-notes template until their official materials are supplied.

---

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full process. In short:

1. Fork the repository and create a new branch.
2. Add or verify resources for a specific week.
3. Update that week's `README.md` and `resource-notes.md`.
4. Update the [roadmap](agentic-ai-24-week/ROADMAP.md) when a week's topic or status changes.
5. Open a pull request with a clear description of what was added or verified.

Be respectful, constructive, and never upload copyrighted or private materials without permission.
