import json
import os

output_path2 = os.path.join("output", "full_response.json")

output_path3 = os.path.join("output", "unique_observation_codes.json")

with open(output_path2) as f:
    bundle = json.load(f)

codes = set()

for entry in bundle.get("entry", []):
    res = entry.get("resource", {})
    if res.get("resourceType") == "Observation":
        for coding in res.get("code", {}).get("coding", []):
            code = coding.get("code")
            display = coding.get("display")
            if code:
                codes.add((code, display))

# Convert the set of tuples to a list of dicts for JSON serialization
codes_list = [{"code": c, "display": d} for c, d in sorted(codes)]

# Write to file
with open(output_path3, "w", encoding="utf-8") as f:
    json.dump(codes_list, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(codes_list)} unique codes to unique_observation_codes.json")