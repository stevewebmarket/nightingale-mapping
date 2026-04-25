import os
from pathlib import Path
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read(path):
    return (ROOT / path).read_text()

def write(path, content):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)

# Load context
manager_rules = read("nmb3/nmb3_manager_agent.md")
interpreter_rules = read("nmb3/nmb3_interpreter_agent.md")
block_template = read("nmb3/nmb3_block_template.md")

latest_report = read("nmb3/nmb3_reports/block_001_report.md")
raw_output = read("nmb3/nmb3_logs/block_001_raw_output.txt")

prompt = f"""
You are the NMB3 Manager + Interpreter Agent.

Rules:
{manager_rules}

Interpreter:
{interpreter_rules}

Block template:
{block_template}

Latest report:
{latest_report}

Raw output:
{raw_output}

Task:
1. Evaluate the report (pass/fail/partial)
2. Decide next block (Block 002)
3. Generate Block 002 plan using the template

Strict rules:
- Stay in M3.1
- One parameter family only
- Do NOT change system design
- Do NOT expand scope

Output ONLY the block plan text.
"""

response = client.responses.create(
    model="gpt-4.1",
    input=prompt,
)

block_text = response.output_text

write("nmb3/nmb3_blocks/block_002_plan.md", block_text)

print("Block 002 generated:")
print(block_text)
