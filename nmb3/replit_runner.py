import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)

# Load context
project_charter = read_file("nmb3/nmb3_project_charter.md")
manager_rules = read_file("nmb3/nmb3_manager_agent.md")
interpreter_rules = read_file("nmb3/nmb3_interpreter_agent.md")
block_template = read_file("nmb3/nmb3_block_template.md")
decision_policy = read_file("nmb3/nmb3_decision_policy.md")
autonomous_loop_policy = read_file("nmb3/nmb3_autonomous_loop_policy.md")

latest_report = read_file("nmb3/nmb3_reports/block_001_report.md")
raw_output = read_file("nmb3/nmb3_logs/block_001_raw_output.txt")

# Build prompt
prompt = f"""
You are the NMB3 Manager + Interpreter Agent.

PROJECT CHARTER:
{project_charter}

MANAGER RULES:
{manager_rules}

INTERPRETER RULES:
{interpreter_rules}

DECISION POLICY (BINDING — overrides any conflicting prior practice):
{decision_policy}

AUTONOMOUS LOOP POLICY (BINDING — governs session-level scope, budget, and stop conditions):
{autonomous_loop_policy}

BLOCK TEMPLATE:
{block_template}

LATEST REPORT:
{latest_report}

RAW OUTPUT:
{raw_output}

Tasks:
1. Evaluate the report (pass/fail/partial)
2. Identify risks
3. Decide next block
4. Generate next block plan using template

Output format:

--- INTERPRETER RESULT ---
...

--- NEXT BLOCK PLAN ---
...
"""

response = client.responses.create(
    model="gpt-4.1",
    input=prompt,
)

output_text = response.output_text

write_file("nmb3/nmb3_reports/manager_output.txt", output_text)

print("Manager output written.")
