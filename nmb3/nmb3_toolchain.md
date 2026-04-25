NMB3 Toolchain Definition

Manager Agent
- Platform: ChatGPT
- Role: creates block plans
- Input: project state + previous reports
- Output: block plan (1 question only)

Execution Agent
- Platform: Cursor (or Claude Code if using that)
- Environment: local Nightingale repo
- Capabilities:
  - run Python scripts
  - edit files
  - create logs and reports
- Constraints:
  - must follow block plan exactly
  - cannot expand scope
  - must stop after block

Interpreter Agent
- Platform: ChatGPT
- Input: block report
- Output:
  - pass/fail judgement
  - risk detection (fake progress, metric gaming)
  - next block recommendation

Repository
- Platform: GitHub
- Structure:
  - nmb3/roles
  - nmb3/blocks
  - nmb3/logs
  - nmb3/reports

Execution Model
- All code runs locally
- No cloud compute (for now)
- No autonomous long-running loops yet

Control Rules
- One block active at a time
- One report per block
- Steve approval required before next block
- No agent may start a new block independently
