NMB3 Replit OpenAI Manager

Purpose:
Run the NMB3 autonomous loop from an online Replit environment.

Source of truth:
The GitHub repository.

The manager must read:
- nmb3/nmb3_project_charter.md
- nmb3/nmb3_roles.md
- nmb3/nmb3_toolchain.md
- nmb3/nmb3_manager_agent.md
- nmb3/nmb3_interpreter_agent.md
- nmb3/nmb3_block_template.md
- latest block plan
- latest block report
- latest raw output

The manager may produce:
- interpreter judgement
- next proposed block plan
- risk warning
- funding relevance update
- GitHub issue or PR text

The manager may not:
- approve its own next block
- change milestone without Steve approval
- make funding claims without evidence
- rewrite core pipeline unless explicitly assigned
- run open-ended exploration

Execution rule:
The Replit runner executes bounded blocks.
The OpenAI Manager interprets and proposes.
Steve approves milestone transitions.

Initial autonomy level:
The system may automatically run M3.1 validation blocks.
The system may propose Block 002, Block 003, and Block 004.
The system must pause before M4 unless Steve approves.
