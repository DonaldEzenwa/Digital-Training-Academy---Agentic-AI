from pathlib import Path
import zipfile
import textwrap

root = Path.cwd() / "agentic-ai-24-week"


def W(content: str) -> str:
    return textwrap.dedent(content).strip() + "\n"


files = {
    "README.md": W("""
        <div align="center">

        # Agentic AI Field Guide

        **A 24-week learning journey - organized resources, hands-on practice, and learning notes.**

        [Start Here](#start-here) · [24-Week Roadmap](ROADMAP.md) · [Weekly Resources](#weekly-resources) · [Contributing](CONTRIBUTING.md)

        </div>

        ---

        > **Project status:** In progress. Weeks 1–2 have resource links recorded. Resource topics and learning outcomes still need to be verified from the source materials.

        ## Start here

        This repository organizes resources for a 24-week Agentic AI training journey. It is designed to make each week's slides, reading materials, hands-on documents, code repositories, and personal notes easy to find.

        ### How to use this guide

        1. Open the relevant week in `weeks/`.
        2. Start with that week's `README.md`.
        3. Open the linked source materials.
        4. Complete the hands-on activity and record your own notes.
        5. Update the checklist and status when finished.

        ## Weekly resources

        | Week | Status | Resource index |
        |---|---|---|
        | [Week 01](weeks/week-01/README.md) | Links recorded; topics to verify | Foundations / source materials |
        | [Week 02](weeks/week-02/README.md) | Links recorded; GitHub destination needs clarification | Slides and hands-on document |
        | Weeks 03–24 | Not yet supplied | Reserved for future resources |

        ## Resource status key

        - `Not started` - not reviewed yet
        - `In progress` - currently studying
        - `Completed` - worked through the material
        - `Reviewed` - link and description checked
        - `Needs access` - source cannot currently be opened

        ## Curation principles

        - Link to original sources rather than copying materials without permission.
        - Clearly distinguish source material from personal notes.
        - Add a short explanation of why each resource is useful after reviewing it.
        - Check links periodically and record when they were last reviewed.
        - Do not claim a resource has been completed or reviewed until it has.

        ## Repository structure

        ```text
        .
        ├── README.md
        ├── ROADMAP.md
        └── weeks/
            ├── week-01/
            │   ├── README.md
            │   ├── resource-notes.md
            │   └── learning-log.md
            ├── week-02/
            │   ├── README.md
            │   ├── resource-notes.md
            │   └── learning-log.md
            └── week-03-to-24/
                ├── README.md
                ├── resource-notes.md
                └── learning-log.md
        ```

        ## Start contributing

        See [CONTRIBUTING.md](CONTRIBUTING.md) for the simple process for adding and checking resources.
    """),
    "ROADMAP.md": W("""
        # 24-Week Agentic AI Learning Roadmap

        This roadmap is a tracking scaffold, **not a claim about the official training curriculum**. Weeks 1 and 2 contain the resource links supplied so far. Their exact topics and outcomes must be confirmed from the linked materials before this roadmap is filled in.

        ## Weekly progress

        | Week | Topic | Status |
        |---|---|---|
        | 01 | To verify from source materials | Links recorded |
        | 02 | To verify from source materials | Links recorded |
        | 03 | Awaiting resources | Not started |
        | 04 | Awaiting resources | Not started |
        | 05 | Awaiting resources | Not started |
        | 06 | Awaiting resources | Not started |
        | 07 | Awaiting resources | Not started |
        | 08 | Awaiting resources | Not started |
        | 09 | Awaiting resources | Not started |
        | 10 | Awaiting resources | Not started |
        | 11 | Awaiting resources | Not started |
        | 12 | Awaiting resources | Not started |
        | 13 | Awaiting resources | Not started |
        | 14 | Awaiting resources | Not started |
        | 15 | Awaiting resources | Not started |
        | 16 | Awaiting resources | Not started |
        | 17 | Awaiting resources | Not started |
        | 18 | Awaiting resources | Not started |
        | 19 | Awaiting resources | Not started |
        | 20 | Awaiting resources | Not started |
        | 21 | Awaiting resources | Not started |
        | 22 | Awaiting resources | Not started |
        | 23 | Awaiting resources | Not started |
        | 24 | Awaiting resources | Not started |

        ## How each week should be documented

        For each week, add:
        - The official topic and learning objectives
        - Slides and reading materials
        - Hands-on exercises and code repositories
        - Prerequisites, if any
        - Key concepts and personal notes
        - A practical deliverable or checkpoint
        - Completion status and last-reviewed date

        Update this roadmap only when the weekly resources or official curriculum confirm the topic.
    """),
}

week01 = {
    "README.md": W("""
        # Week 01 - Resource Index

        **Status:** Links recorded; source contents not yet verified  
        **Official week title:** To be confirmed from the materials

        ## Source materials

        | Resource | Type | Link | Review status |
        |---|---|---|---|
        | Week 1 resource document | Google Doc | [Open document](https://docs.google.com/document/d/1zcseX_Y3L6AhCB3RTdyJg1fUe-XUQFQtMIhkg2nSR6o/edit?tab=t.0) | Needs content review |
        | Week 1 Canva material | Canva design | [Open design](https://www.canva.com/design/DAHXI3TXQf0/RLkq3ACk8xdsi7tN3J6n6A/edit) | Needs content review |
        | Week 1 presentation | Google Slides | [Open slides](https://docs.google.com/presentation/d/1P5tT_zEwMmrhfRLjK5oco8Jt60uy70m4/edit?slide=id.p29) | Needs content review |

        ## Learning objectives

        _To be filled in after reviewing the source materials. Do not infer the official objectives from link types alone._

        ## Suggested workflow

        - [ ] Review the resource document.
        - [ ] Review the Canva material.
        - [ ] Review the presentation.
        - [ ] Record the official week title and learning objectives.
        - [ ] Add a concise resource summary to `resource-notes.md`.
        - [ ] Record questions, lessons, and practical work in `learning-log.md`.

        ## Related files

        - [Resource notes](resource-notes.md)
        - [Learning log](learning-log.md)
    """),
    "resource-notes.md": W("""
        # Week 01 - Resource Notes

        > Complete these notes after opening and reviewing the original resources.

        ## Official topic

        _To verify._

        ## Key concepts

        - To be added after review.

        ## Resource-by-resource notes

        ### 1. Week 1 resource document

        - **Link:** https://docs.google.com/document/d/1zcseX_Y3L6AhCB3RTdyJg1fUe-XUQFQtMIhkg2nSR6o/edit?tab=t.0
        - **What it covers:** To verify.
        - **Useful takeaways:** To add.
        - **Questions:** To add.

        ### 2. Week 1 Canva material

        - **Link:** https://www.canva.com/design/DAHXI3TXQf0/RLkq3ACk8xdsi7tN3J6n6A/edit
        - **What it covers:** To verify.
        - **Useful takeaways:** To add.
        - **Questions:** To add.

        ### 3. Week 1 presentation

        - **Link:** https://docs.google.com/presentation/d/1P5tT_zEwMmrhfRLjK5oco8Jt60uy70m4/edit?slide=id.p29
        - **What it covers:** To verify.
        - **Useful takeaways:** To add.
        - **Questions:** To add.

        ## My summary

        _Write a short explanation in your own words after reviewing the materials._
    """),
    "learning-log.md": W("""
        # Week 01 - Learning Log

        - **Date started:** 
        - **Date completed:** 
        - **Status:** Not started

        ## What I learned

        _Add your own notes._

        ## What I practiced

        _Record exercises or implementation work._

        ## What confused me

        _List questions to revisit._

        ## Evidence / deliverable

        _Link a notebook, code sample, screenshot, or project when appropriate. Avoid uploading confidential or restricted course materials._
    """),
}

week02 = {
    "README.md": W("""
        # Week 02 - Resource Index

        **Status:** Links recorded; source contents not yet verified  
        **Official week title:** To be confirmed from the materials

        ## Source materials

        | Resource | Type | Link | Review status |
        |---|---|---|---|
        | Week 2 slides | Google Slides | [Open slides](https://docs.google.com/presentation/d/1X3-hC88pISr2zKGAqcNN9cEKqs_Ny0PT/edit?usp=sharing&ouid=106370953992675903899&rtpof=true&sd=true) | Needs content review |
        | Week 2 hands-on document | Google Doc | [Open hands-on document](https://docs.google.com/document/d/1wJbBtZ0uD2mYNdpKZgM3i-vDH6-M3t8YdhWp9ElofZA/edit?usp=sharing) | Needs content review |
        | GitHub repository | GitHub | [GitHub home supplied](https://github.com/) | Specific repository URL needed |

        ## Learning objectives

        _To be filled in after reviewing the source materials._

        ## Suggested workflow

        - [ ] Review the slides.
        - [ ] Review the hands-on document.
        - [ ] Replace the generic GitHub link with the exact repository URL.
        - [ ] Record the official week title and learning objectives.
        - [ ] Add a concise summary to `resource-notes.md`.
        - [ ] Record practical work and reflections in `learning-log.md`.

        ## Related files

        - [Resource notes](resource-notes.md)
        - [Learning log](learning-log.md)
    """),
    "resource-notes.md": W("""
        # Week 02 - Resource Notes

        > Complete these notes after opening and reviewing the original resources.

        ## Official topic

        _To verify._

        ## Resource-by-resource notes

        ### 1. Week 2 slides

        - **Link:** https://docs.google.com/presentation/d/1X3-hC88pISr2zKGAqcNN9cEKqs_Ny0PT/edit?usp=sharing&ouid=106370953992675903899&rtpof=true&sd=true
        - **What it covers:** To verify.
        - **Useful takeaways:** To add.
        - **Questions:** To add.

        ### 2. Week 2 hands-on document

        - **Link:** https://docs.google.com/document/d/1wJbBtZ0uD2mYNdpKZgM3i-vDH6-M3t8YdhWp9ElofZA/edit?usp=sharing
        - **What it covers:** To verify.
        - **Hands-on task / expected output:** To verify.
        - **Useful takeaways:** To add.
        - **Questions:** To add.

        ### 3. GitHub repository

        - **Link supplied:** https://github.com/
        - **Specific repository:** Needed.
        - **Purpose:** To verify.

        ## My summary

        _Write a short explanation in your own words after reviewing the materials._
    """),
    "learning-log.md": W("""
        # Week 02 - Learning Log

        - **Date started:** 
        - **Date completed:** 
        - **Status:** Not started

        ## What I learned

        _Add your own notes._

        ## Hands-on work

        - **Task:** To verify from the source document.
        - **What I built or tried:** 
        - **Result / repository link:** 

        ## What confused me

        _List questions to revisit._

        ## Evidence / deliverable

        _Link your own implementation or notes when appropriate. Do not republish restricted course materials._
    """),
}

template = {
    "README.md": W("""
        # Weekly Resource Template

        Copy this folder for each upcoming week and rename it `week-03`, `week-04`, and so on through `week-24`.

        **Official week title:**  
        **Status:** Not started  
        **Date / schedule:**  

        ## Learning objectives

        - To be added from the official materials.

        ## Resources

        | Resource | Type | Link | Why it matters | Status |
        |---|---|---|---|---|
        | Resource 1 | To classify | Add link | Add after review | Not started |

        ## Weekly checklist

        - [ ] Review all assigned resources.
        - [ ] Complete the hands-on task.
        - [ ] Record notes and questions.
        - [ ] Link any personal deliverable.
        - [ ] Update the roadmap.
    """),
    "resource-notes.md": W("""
        # Weekly Resource Notes

        ## Official topic

        _To verify from source materials._

        ## Key concepts

        _To add after review._

        ## Notes by resource

        _Add a subsection for each resource, including its link, purpose, useful takeaways, and questions._

        ## My summary

        _Write in your own words._
    """),
    "learning-log.md": W("""
        # Weekly Learning Log

        - **Date started:** 
        - **Date completed:** 
        - **Status:** Not started

        ## What I learned

        ## What I practiced

        ## Questions to revisit

        ## Deliverable / evidence

        ## Next steps
    """),
}

all_files = dict(files)

for fname, content in week01.items():
    all_files[f"weeks/week-01/{fname}"] = content

for fname, content in week02.items():
    all_files[f"weeks/week-02/{fname}"] = content

for fname, content in template.items():
    all_files[f"weeks/week-03-to-24-template/{fname}"] = content

for n in range(3, 25):
    week = f"week-{n:02d}"
    for fname, content in template.items():
        all_files[f"weeks/{week}/{fname}"] = content

for rel, content in all_files.items():
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

print(f"Created {len(all_files)} files under {root}")

zip_path = Path.cwd() / "agentic-ai-24-week.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for p in root.rglob("*"):
        if p.is_file():
            zf.write(p, p.relative_to(root.parent))

print(f"Packaged to {zip_path}")
