import os
import requests
import json

output_path = os.path.join("output", "full_response.json")
output_path2 = os.path.join("output", "results.json")
url = "http://host.docker.internal:8585/fhir/r4"
localhosturl = "http://localhost:8585/fhir/r4"

# Read the JSON bundle from file
with open(output_path, "r") as f:
    bundle = json.load(f)

# Send the bundle as a POST request
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, json=bundle)
# Print the response from the server
print('response.status_code')
print(response.status_code)
print(response.text)
print('response.status_code')
with open(output_path2, "w", encoding="utf-8") as f:
    f.write(response.text)



