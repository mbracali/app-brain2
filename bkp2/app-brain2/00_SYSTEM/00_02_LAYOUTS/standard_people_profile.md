> [!Example] Profile layout — instructions for the agent
>
> **Filename**
> - Format: `FIRSTNAME_LASTNAME.md`. UPPER CASE, ASCII only (strip diacritics: `João` → `JOAO`). Spaces and punctuation become `_`. **Never use double underscores** — collapse any repeats to a single `_`.
> - If only a first name is known, use it alone (`JOAO.md`). If only a nickname is known, use it as-is in upper case and record the real name in ALIASES later.
> - **Disambiguation chain** when the filename collides:
>   1. Append the **full FROM value**, upper-cased, words joined by single underscores: `JOAO_SILVA_COMPANY_X.md`. Use the complete company/school/event name — never an abbreviation or just one part of it.
>   2. If still colliding, append an integer with a single underscore: `JOAO_SILVA_COMPANY_X_2.md`.
>
> **Identity check before creating a new file**
> - Before creating a profile, scan existing files in `01_PEOPLE/01_00_DATABASE/` for a probable match using FULL NAME, ALIASES, and FROM.
> - If a match is found, update the existing file. If the match is ambiguous, do NOT create a new file — write a question to `98_TRANSIENT/98_03_REVIEW/questions.md` and skip this person until the question is answered.
>
> **Header table**
> - FULL NAME — written as known, accents preserved (the filename is the only place that strips them).
> - ALIASES — nicknames, alternate spellings, maiden names. Comma-separated. Used for future identity matching.
> - FROM — context where Marcelo first connected with this person (`Company_X`, `school_Y`, `Event_Z`). Multiple values pipe-separated.
> - COUNTRY — country of origin or current residence; pick whichever is more relevant. Note the other in DESCRIPTION if needed.
> - ROLE — occupation or title.
> - LANGUAGES — languages spoken, comma-separated.
> - DESCRIPTION — single line, max 30 words, no newlines.
>
> **CONTACTS** — one row per contact. `TYPE` is the channel (phone, email, instagram, linkedin, whatsapp, telegram, etc.). `LABEL` is its purpose (work, personal, mom's, etc.) — use `—` if not applicable. `VALUE` is the actual contact data.
>
> **RELATIONS** — one per line: `- [[PERSON_FILENAME]] — relation type` (e.g. `- [[JOAO_SILVA]] — brother`). Use the `[[link]]` form only, no `.md` extension. When you record a relation in person A's file, mirror it in person B's file.
>
> **PERSONALITY** — traits, likes, dislikes, preferences, behavioral facts. Plain bullet list allowed. No nested bullets, no headings, no decorations.
>
> **NOTABLE FACTS** — facts ABOUT the person (life events, milestones, status changes). NOT interactions between the person and Marcelo — those live elsewhere. Format each line: `- YYYY-MM-DD — <fact>`.
>
> **Tags** — at the bottom of the file, after all sections. Format: `#tag #tag`. Lowercase, underscored.
>
> **Empty sections** — always include every section of the template. Sections with no data keep their header with blank content. The template below is the required shape, not the maximum shape.

---

# %PERSON FULL NAME%

| FIELD       | VALUE |
| ----------- | ----- |
| FULL NAME   |       |
| ALIASES     |       |
| FROM        |       |
| COUNTRY     |       |
| ROLE        |       |
| LANGUAGES   |       |
| DESCRIPTION |       |

## CONTACTS

| TYPE | LABEL | VALUE |
| ---- | ----- | ----- |
|      |       |       |

## RELATIONS

## PERSONALITY

## NOTABLE FACTS

#tag
