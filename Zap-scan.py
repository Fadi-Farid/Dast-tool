import torch
import time
import requests
from zapv2 import ZAPv2
from requests.exceptions import ProxyError
import json


# Initialize ZAP API client with API key
api_key = 'vh7bqrauhothh2b0en7r53se5i'
zap = ZAPv2(apikey=api_key)

# Take target URL as input
target = "http://13.216.2.173:5000"
code = "https://github.com/Fadi-Farid/python-web-app/tree/main"
# Crawl and scan web application
zap.spider.scan(target)
scan = zap.ascan.scan(target)


#print(f'Scan started with ID: {scan}')
while int(zap.ascan.status(scan)) < 100:
    print(f'Scan progress: {zap.ascan.status(scan)}%')
    time.sleep(5)
scan_results = zap.core.alerts(target)
print(f'Scan results: {scan_results}')

# Check the status of the scan
print("✅ Scan results is generated.")

report = []
new_report = scan_results[:1]
i=0
for item in new_report:
    i=i+1
    description = item["description"]
    reference = item["reference"]
    solution_provided = item["solution"]
    url = "http://3.236.245.215/api/generate"
    payload = {
     "model": "llama3",
     "prompt": (
      f"Vulnerability Reference: {reference}\n"
      f"Description: {description}\n"
      f"ZAP Recommendation: {solution_provided}\n"
      f"Fix Required: Please provide the necessary code changes and specify the file name where the changes should be applied with the updated code in the repository '{code}'"
     ),
     "stream": False
    }

    solution = requests.post(url, json=payload)


    response_json = solution.json()
    readable_output = response_json["response"].encode().decode("unicode_escape")
    print(readable_output)

    report_entry = {
        "Vulnerability_No": i,
        "Name" : item["name"],
        "url": item["url"],
        "risk": item["risk"],
        "tags" : item["tags"],
        "solution": readable_output
    }
    print(f'✅ Solution is generated for Vulnerability_No: {i}.')
    report.append(report_entry)
# Save DAST report to file
