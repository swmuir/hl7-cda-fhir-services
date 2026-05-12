import os
import requests

# --- Configuration ---
base_url = "http://host.docker.internal:8989/cdaservices"
document_id = "DeduplicatedCDA"
medicaid = "M456"
patient_id = "examplePatient123"
output_path = os.path.join("output", "serviceEventIndex.json")

url = f"{base_url}/getDocumentIndex/{document_id}"


# Optional: body content if needed (may be empty)
payload = ""
headers = {
    "Content-Type": "text/json"
}

# --- Send POST request ---
response = requests.get(url,  headers=headers)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Saved full serviceEventIndex to {output_path}")

# --- Print response ---
#print("Status Code:", response.status_code)
#print("Response Body:\n", response.text)
