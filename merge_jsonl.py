import os
import json

jsonl_folder = "jsonl"
merged_file = "merged_adnd_dataset.jsonl"

merged_data = []

for filename in os.listdir(jsonl_folder):
    if filename.endswith(".jsonl"):
        filepath = os.path.join(jsonl_folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        qa = json.loads(line)
                        merged_data.append(qa)
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON from {filepath}: {e}")

with open(merged_file, "w", encoding="utf-8") as f:
    for qa in merged_data:
        f.write(json.dumps(qa, ensure_ascii=False) + "\n")

print(f"{len(merged_data)} QA pairs merged into {merged_file}.")
