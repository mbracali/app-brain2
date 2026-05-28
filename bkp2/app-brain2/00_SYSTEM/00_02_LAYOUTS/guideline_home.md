# Home — content guideline

> [!Note] This is a **guideline**, not a strict template.
> Describes the content that lives in `02_PERSONAL/02_02_HOME/` and suggests common shapes. Adapt to the actual content.

Captures everything related to Marcelo's home: items he owns, items he wants to buy for the home, maintenance notes.

## What goes here

- **Inventory** — furniture, appliances, electronics. What he has, when bought, for how much, model/links.
- **Buy list** — things planned for the home, with reason, link, price.
- **Maintenance / fixes** — things that need to be repaired or upgraded, with status.

## Suggested shapes

Common table starting points:

- Inventory: `Item | Model/Link | Description | Bought at | Value | OBS`
- Buy list: `Description | Reason | Link | Price | OBS`
- Maintenance: `Item | Issue | Status | OBS`

A single file can carry multiple sections with their own tables (e.g. one "Furniture, appliances and related" file with `## Inventory` and `## To buy` sections).

## Filenames

Human-readable. Examples: `Furniture, appliances and related.md`, `Maintenance log.md`.

## Cross-references

People → `01_PEOPLE/index.md` as `[[PERSON_FILENAME|Display Name]]`. Items tied to a person/event reference the person via the canonical link; never create a stub link.
