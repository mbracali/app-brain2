# Project Context: app-brain2

## What This Is

A personal note-keeping system for Marcelo Bracali, designed to be operated by a chain of AI agents. Marcelo dumps raw content (notes, files, voice transcriptions, etc.) into an inbox folder. Agents process, organize, and store that content into a structured markdown vault, viewed via Obsidian.

The project lives in a folder called `app-brain2/` and is under git version control.

## Naming Conventions
**Folders** → `NUMBER_NAME` using `_` as separator
- e.g. `98_TRANSIENT`, `04_WORK`
**Subfolders** → `PARENTNUMBER_NUMBER_NAME`
- e.g. `98_00_INBOX`, `00_03_WORKDIR`
**Numbers** → always zero-padded two digits. `99` is reserved for special/meta items.
**Files** → `lowercase_with_underscores.md`
- e.g. `topic_people_info.md`, `questions.md`, `project_tree.md`

## Agent planning
The system uses a chain of agents. Each agent has a defined scope

### L1 AGENTS
Master agents work more broadly to organize and process the raw content

- L1 — TRIAGE-MASTER (v0.7)
    - Status: Done
    - Reads everything in `98_00_INBOX/` and answered questions in `98_03_REVIEW/questions.md`
    - Triages, converts to markdown, organizes by topic
    - Routes reference assets (manuals, books) to `03_STUDY/03_00_LIBRARY/<theme>/`
    - Writes structured topic files to `98_01_STAGING/`
    - Flags ambiguous content to `98_03_REVIEW/questions.md`
    - Discards useless content to `98_02_SCRATCH/`
    - Compresses processed content to `00_SYSTEM/00_00_ARCHIVE/<YYYY-MM-DD>_compressed.md`
    - Clears the content of `.md` files in `98_00_INBOX/` after archiving (files themselves remain)
    - Uses `00_03_WORKDIR/` as a scratchpad (cleared each run)
    - Spawns sub-agents when the inbox is too large for a single context

- L1 - CONTENT-FORMATER
    - Status: To be built, to be planned
    - This agent will look into the project structure and verify if everything is in order

- L1 - JOURNAL-BUILDER
    - Status: To be built, to be planned
    - This one will format the output for the end user

### L2 AGENTS
Agents that work on specific domains and have strict rules to follow

- L2 - PEOPLE-EXPERT (v0.3)
    - Status: Initial prototype
    - Agent to work on top of the people domain

- L2 - PERSONAL-EXPERT
    - Status: To be built, to be planned
    - Agent to work on top of the personal domain

- L2 - HOME-EXPERT
    - Status: To be built, to be planned
    - Agent to work on all the home related content of the user

- L2 - FEEDBACK-EXPERT
    - Status: To be built, to be planned
    - Agent to work on all the feedback related content of the user

- L2 - FINANCES-EXPERT
    - Status: To be built, to be planned
    - Agent to work on all the finance related content of the user

- L2 - STUDY-EXPERT
    - Status: To be built, to be planned
    - Agent to work on all the study related content of the user

- L2 - WORK-EXPERT
    - Status: To be built, to be planned
    - Agent to work on all the work related content of the user


> More agents can be build in the future if necessary. This document need to be updated from time to time to reflect the current status of the system.

---

## Topic Files (L1 Output → STAGING)

These are the files L1 produces. L2 agents consume them.

| File | Content |
|---|---|
| `topic_people_info.md` | People: full name, traits, contact, connections |
| `topic_meetings_info.md` | Meetings, encounters, conversations: who, when, where, what was discussed |
| `topic_feedbacks_info.md` | Explicit feedback (praise, criticism, suggestions) given or received by Marcelo. NOT meeting summaries |
| `topic_finance_info.md` | Financial info: purchases, sales, prices, stocks, crypto, real estate, expenses, revenue |
| `topic_home_info.md` | Home-related info, current or future properties |
| `topic_personal_info.md` | Personal life: accounts, CV, presentations, goals |
| `topic_study_info.md` | Studies: courses, cheat sheets, references. Audit entries for reference assets routed to `03_LIBRARY/` |
| `topic_work_company_info.md` | Companies: products, services, projects, customers. Per person: name, role, contact |
| `topic_work_personal_info.md` | Personal projects: features, tech details, purpose, audience. Per person: name, role, contact |

> New topics can be added in the future if necessary. This document need to be updated from time to time to reflect the current status of the system.

---

## L2 Agent Rules
- After processing its domain topic file from `98_01_STAGING/`, the L2 agent must delete that file. The compressed archive in `00_00_ARCHIVE/` is the recovery source.
- When writing a file based on a layout from `00_02_LAYOUTS/`, write the full layout structure. Sections with no data keep their header with blank content — never omit them.

---

## Index Graph
Every directory in the vault that holds domain content has an `index.md` file. Indices form a navigable tree that lets you reach any file in `O(depth)` hops from any starting index:

- A directory whose contents are leaf files has an `index.md` listing those files (with `[[Filename]]` links).
- A directory whose contents are subdirectories has an `index.md` listing only the child indices (with `[[Subfolder/index]]` links), not their files.
- A parent index never enumerates a grandchild's files. That responsibility stays with the grandchild's own index.

Indices are agent-rebuilt from scratch on every run — the underlying files are the source of truth, the index is derived. From any `index.md`, navigation should reach every file in that subtree without dead ends.

---

## Questions Loop

When L1 cannot process a note it writes to `98_03_REVIEW/questions.md` using this format:

```
## [YYYY-MM-DD HH:MM] Question about: <short description>

**Source file:** <original filename>
**Issue:** <what is unclear, with enough context to resume later>
**Question:** <specific question for Marcelo>
**Answer:**
**Status:**
```

Marcelo fills `**Answer:**`. On the next run, L1 reads it, evaluates it, and either promotes it to STAGING or writes a follow-up. Processed blocks are stamped `**Status:** PROCESSED - YYYY-MM-DD HH:MM`.

---

## Logging
The log pipeline is not implemented yet. In the future it will be implemented using python and should log all agents activities.

---

## General Rules Across All Agents
- All output in **English**. Proper nouns stay in their original language.
- Marcelo may write in Portuguese, Spanish, or English.
- Obsidian-compatible syntax: `[[file_name]]` for links, `#` for headers, `#tag` for tags.
- All dates: `YYYY-MM-DD HH:MM`.
- Agents only read/write paths explicitly listed in their permissions.
- No reasoning or conclusions on top of notes — organize only.
- No speculative file or section creation.

