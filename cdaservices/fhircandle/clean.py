import json

with open("full_response.json") as f:
    b = json.load(f)

b["entry"] = [
    e for e in b["entry"]
    if e.get("resource", {}).get("resourceType") != "DiagnosticReport"
]

with open("bundle-clean.json", "w") as f:
    json.dump(b, f, indent=2)