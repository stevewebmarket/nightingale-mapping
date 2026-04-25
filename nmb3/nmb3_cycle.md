NMB3 Operating Cycle

Cycle length:
12 hours (after initial testing phase)

Cycle structure:

1. Steve approves a block plan
2. Execution Agent runs the block
3. Execution Agent writes report
4. System pauses
5. Interpreter Agent evaluates report
6. Steve reviews:
   - Did it answer the question?
   - Is the result real?
   - Did the agent stay within bounds?
   - Are we closer to funding-grade proof?
   - What is the next block?

Rules:

- Only one block may be active at a time
- Every block must answer one question
- Every block must produce a report
- No block may start without Steve approval
- Execution Agent must stop after report

Mid-block control:

- After every ~5 runs:
  - check: "Am I still answering the block question?"
  - if not: reset to block goal

Naming:

- Blocks: block_001, block_002, etc.
- Plans: nmb3_blocks/
- Reports: nmb3_reports/
- Logs: nmb3_logs/

Initial constraint:

- First blocks should be 2–3 hours
- Only move to 12-hour cycles after clean execution
