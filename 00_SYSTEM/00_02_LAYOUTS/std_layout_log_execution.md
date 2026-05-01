
### Full markdown layout for execution

Final file, should only have the content of the code block.

```

> [!Example] Log guidelines - Table columns and formats
> - DATE: The date, hour and minute of that entry
> 	- Format: YYYY-MM-DD HH:MM
> 	- Example: `2026-04-01 12:10`
> - AGENT: The name of the agent that performed that entry
> 	- Format: "AGENT_LEVEL - AGENT_NAME"
> 	- Example 1: `L1 - TRIAGE_AGENT`
> - OPERATION: Class of operation performed, with the following possible values
> 	- CREATE = When creating a file
> 	- DELETE = When deleting a file
> 	- EDIT = When editing a file
> 	- FINISH = When the agent finished its processing
> 	- START = When the agent started its processing
> - ACTION: Description of what was done, file created, moved or anything else.
> 	- Format: 20 chars max, string
> 	- Example: "File x.md created"
> - ERROR: Column stating if the operation had any error
> 	- Format: "YES" or "NO" 

| DATE             | AGENT             | OPERATION | ACTION                            | ERROR |
| ---------------- | ----------------- | --------- | --------------------------------- | ----- |
| 2026-04-01 12:10 | L1 - TRIAGE_AGENT | START     | Looking into the transient folder | --    |
| 2026-04-01 18:42 | L1 - TRIAGE_AGENT | END       | Nothing to add, finishing         | --    |
| 2026-05-01 08:00 | L1 - TRIAGE_AGENT | START     | Looking into the, review folder   | --    |
```

