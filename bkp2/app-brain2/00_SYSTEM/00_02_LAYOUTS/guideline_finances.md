# Finances — content guideline

> [!Note] This is a **guideline**, not a strict template.
> Describes the content that lives in `02_PERSONAL/02_01_FINANCES/` and suggests common shapes. Adapt to the actual content.

Captures Marcelo's money: recurring bills and costs, investments, mentorship/learning notes about money, and things he wants to buy.

## What goes here

- **Bills and recurring costs** — monthly/yearly payments: who they're paid to, how, when, and roughly how much.
- **Investments** — positions held, planned positions, allocation strategies.
- **Investment learning** — notes from courses, books, or mentorships about money.
- **Things to buy** — wishlists with description, reason, link, price, notes.

## Suggested shapes

**Tables** with descriptive columns:

- Bills: `Description | Type | Sub-type | Pay to | How to pay | Pay at | Average cost | OBS`
- Buy list: `Description | Reason to buy | Link | Price | Notes`
- Investment positions: `Type | Asset | Allocation | Last yield | Notes`

**Multi-section files.** Investment-mentorship-style content uses `# Class N — topic` headers with one or more tables under each. Keep classes/sections in chronological order.

Use Markdown lists or short paragraphs inside table cells when a single cell needs structure. Keep cells reasonably short — split into a new section if a cell becomes a wall of text.

## Filenames

Human-readable. Examples: `Bills and costs.md`, `Stuff to buy.md`, `Investment mentorship - 2025.md`.

## Cross-references

People → `01_PEOPLE/index.md` as `[[PERSON_FILENAME|Display Name]]`. Companies and services that don't have a profile elsewhere render as plain text.
