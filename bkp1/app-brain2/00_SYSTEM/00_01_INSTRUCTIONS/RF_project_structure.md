

```
app-brain2/
├── 00_SYSTEM/                 # > System wide related files
│   ├── 00_00_ARCHIVE/         # -> Store backup of transient files
│   ├── 00_01_INSTRUCTIONS/    # -> Instructions for agents and sub-agents
│   ├── 00_02_LAYOUTS/         # -> Folder with all the standard layouts
│   ├── 00_03_WORKDIR/         # -> Temporary scratchpad during processing (cleared each run)
│   └── 00_99_LOGS/            # -> Log of all changes and exceptions
│
├── 01_PEOPLE/                 # > People and contacts files
│   └── 01_00_DATABASE/        # -> One file per each person in the database
│
├── 02_PERSONAL/               # > Personal related files
│   ├── 02_00_PERSONAL_INFO/   # -> Personal info files
│   ├── 02_01_FINANCES/        # -> Finances files
│   ├── 02_02_HOME/            # -> Home files
│   └── 02_03_FEEDBACKS/       # -> Feedbacks files
│
├── 03_STUDY/                  # -> Study related files
│
├── 04_WORK/                   # -> Work related files
│   ├── 04_00_GENERICS/        # -> Generic info about companies
│   ├── 04_01_COMPANIES/       # -> Companies Marcelo works for or has worked for
│   └── 04_02_PERSONAL/        # -> Personal projects Marcelo is working on or has worked on
│
├── 98_TRANSIENT/              # -> Temporary processing area
│   ├── 98_00_INBOX/           # -> Raw, unsorted incoming content (read-only for this agent)
│   ├── 98_01_STAGING/         # -> Processed topic files ready for the next agent
│   ├── 98_02_SCRATCH/         # -> Useless or throwaway content
│   └── 98_03_REVIEW/          # -> Needs human decision before moving
│
└── 99_OUTPUT/                 # -> Outgoing, polished content for humans
    ├── 99_00_HOME/            # -> Main outputs for Marcelo
    └── 99_01_SCRIPTS/         # -> Outputted scripts, codes, etc
```
