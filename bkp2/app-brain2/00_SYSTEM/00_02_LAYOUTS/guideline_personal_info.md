# Personal Info — content guideline

> [!Note] This is a **guideline**, not a strict template.
> It describes the kinds of content that live in `02_PERSONAL/02_00_PERSONAL_INFO/` and suggests common shapes. Adapt to the actual content. Add columns, sections, or new file types when needed; drop them when not.

The personal info subfolder captures identity-level information about Marcelo: who he is, his accounts, his important documents, his CV, his goals, and useful references he wants to remember.

## What goes here

- **Identity / "about me"** — short intros Marcelo uses to introduce himself in different contexts.
- **Accounts and credentials** — service accounts, online identities, identifiers (Pix keys, usernames, email-per-service).
- **Documents** — government IDs, professional documents, registration numbers.
- **CV** — work history, education, skills, certifications. May be one long file or split per version.
- **Goals** — year-scoped or topic-scoped goals with status.
- **Useful sites** — bookmarks, references, learning resources.

Each topic typically lives in its own small, focused file.

## Suggested shapes

Most content fits a Markdown table with descriptive columns. Common starting columns:

- Accounts: `Provider | Service | Identifier | Notes`
- Documents: `Type | Name | Number | OBS`
- Goals: `Goal | Description | Status | OBS`
- Sites: `Name | URL | Topic | Notes`

Use `##` headers when a file has more than one logical group (e.g. an "Accounts" file with separate sections for Pix keys, service accounts, emergency keys).

CV-style files are an exception — they use prose with `##` headers per section (Summary, Skills, Education, Experience), not tables.

## Filenames

Human-readable, descriptive. Mixed case and spaces are allowed. Examples: `Accounts and docs.md`, `Personal goals - 2026.md`, `Curriculum 12-2025.md`. Match the existing naming style in this subfolder when extending an established type.

## Cross-references

People mentions resolve through `01_PEOPLE/index.md` as `[[PERSON_FILENAME|Display Name]]`. If a person isn't catalogued, render the name as plain text — never a stub link.
