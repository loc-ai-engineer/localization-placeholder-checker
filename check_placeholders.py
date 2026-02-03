import json
import re

PLACEHOLDER_PATTERN = re.compile(r"\{[^}]+\}")

def extract_placeholders(text):
    return set(PLACEHOLDER_PATTERN.findall(text))

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def check_placeholders(source, target):
    issues = []

    for key, source_text in source.items():
        target_text = target.get(key)

        if not target_text:
            issues.append(f"Missing key in target: {key}")
            continue

        source_ph = extract_placeholders(source_text)
        target_ph = extract_placeholders(target_text)

        if source_ph != target_ph:
            issues.append(
                f"Placeholder mismatch in '{key}': "
                f"source={source_ph}, target={target_ph}"
            )

    return issues

if __name__ == "__main__":
    source_data = load_json("source.json")
    target_data = load_json("target.json")

    problems = check_placeholders(source_data, target_data)

    if problems:
        print("Issues found:")
        for p in problems:
            print("-", p)
    else:
        print("No placeholder issues found.")
