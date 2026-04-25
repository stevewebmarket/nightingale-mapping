import os
from pathlib import Path
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]

required_files = [
    "nmb3/nmb3_manifesto.md",
    "nmb3/nmb3_roles.md",
    "nmb3/nmb3_toolchain.md",
    "nmb3/nmb3_manager_agent.md",
    "nmb3/nmb3_interpreter_agent.md",
    "nmb3/nmb3_decision_policy.md",
    "nmb3/nmb3_autonomous_loop_policy.md",
    "nmb3/nmb3_block_template.md",
    "nmb3/nmb3_blocks/block_001_plan.md",
]

missing = []

for file_path in required_files:
    if not (ROOT / file_path).exists():
        missing.append(file_path)

if missing:
    print("Missing required files:")
    for item in missing:
        print(f"- {item}")
    raise SystemExit(1)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise SystemExit("OPENAI_API_KEY not found in environment.")

client = OpenAI(api_key=api_key)

context = "\n\n".join(
    f"--- {file_path} ---\n{(ROOT / file_path).read_text()}"
    for file_path in required_files
)

prompt = f"""
You are the NMB3 Manager Agent.

Confirm that you can read the project operating files below.
Then summarize:
1. current objective
2. current milestone
3. current active block
4. what the next system action should be

PROJECT FILES:
{context}
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
)

output = response.output_text

out_path = ROOT / "nmb3/nmb3_reports/replit_manager_smoke_test.md"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(output)

print("Smoke test passed.")
print(f"Wrote: {out_path}")
print()
print(output)
