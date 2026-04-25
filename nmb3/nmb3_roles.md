NMB3 Roles Definition

Steve (Operator)
- Approves every 12-hour block
- Decides milestone transitions
- Judges whether progress is real
- Cannot be bypassed

Manager Agent (ChatGPT)
- Defines block plans
- References current milestone (M3.1, M4, etc.)
- Prevents drift
- Outputs ONE clear next action
- Cannot execute code

Execution Agent (Cursor / Claude Code)
- Runs code
- Edits files (only within constraints)
- Logs all actions
- Writes report
- MUST stop after block
- Cannot define new direction

Interpreter Agent (ChatGPT)
- Evaluates report
- Decides if result is real or fake
- Flags metric gaming or drift
- Recommends next block
- Cannot approve its own plan

System Constraints
- Max 3 agents active
- No agent may self-approve next phase
- Every block must answer ONE question
- Every block must produce a report
- No uncontrolled exploration
