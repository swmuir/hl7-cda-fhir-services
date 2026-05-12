import os
import requests

#http://localhost:8080/cdaservices
# Configuration
base_url = "http://host.docker.internal:8989/cdaservices"
directory_path = "./TestData"  # Directory containing XML files
#patient_id = "examplePatient123"  # Set to None if you want to omit



headers = {
    "Content-Type": "text/xml"
}


import os
import random
import requests

# Configuration
base_url = "http://host.docker.internal:8989/cdaservices"
directory_path = "./TestData"  # Directory containing XML files
max_files = 10

headers = {
    "Content-Type": "text/xml"
}

# List all XML files
all_files = [f for f in os.listdir(directory_path) if f.lower().endswith(".xml")]

# Randomly pick up to max_files files
#selected_files = random.sample(all_files, min(max_files, len(all_files)))
selected_files = random.sample(all_files, 1) if all_files else []

for filename in selected_files:
    document_id = 'DeduplicatedCDA'
    file_path = os.path.join(directory_path, filename)

    # Read XML content
    with open(file_path, "r", encoding="utf-8") as file:
        xml_content = file.read()

    # Build URL and params
    url = f"{base_url}/addDocument/{document_id}"
    params = {"patientId": filename} if filename else {}

    # POST request
    try:
        response = requests.post(url, headers=headers, params=params, data=xml_content)
        print(f"Sent {filename} -> Status: {response.status_code}, Response: {response.text}")
    except requests.RequestException as e:
        print(f"Failed to send {filename}: {e}")

print(f"Processed {len(selected_files)} files.")



