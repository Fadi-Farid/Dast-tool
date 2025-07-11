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
