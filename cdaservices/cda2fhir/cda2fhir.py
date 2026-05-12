import requests
import os

output_path = os.path.join("output", "full_response.xml")

output_path2 = os.path.join("output", "full_response.json")

url = "http://host.docker.internal:8282/mdmi/transformation?source=CDAR2.ContinuityOfCareDocument&target=FHIRR4JSON.MasterBundle"

payload = {}
files=[
  ('message',('Giovanni386.xml',open(output_path,'rb'),'text/xml'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

#print(response.text)

with open(output_path2, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Saved full response to {output_path2}")