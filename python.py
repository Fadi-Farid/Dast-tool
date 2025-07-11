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

with open("dast_report.txt", "w") as f:
    for entry in report:
        f.write(f"Vulnerability No: {entry['Vulnerability_No']}\n")
        f.write(f"Name: {entry['Name']}\n")
        f.write(f"URL: {entry['url']}\n")
        f.write(f"Risk: {entry['risk']}\n")
        f.write(f"Tags: {', '.join(entry['tags'])}\n")
        f.write(f"{entry['solution']}\n")
        f.write("\n" + "-"*80 + "\n")
line_to_remove = "What is the best mitigation strategy for this vulnerability with steps for python?"

with open("dast_report.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

with open("dast_report.txt", "w", encoding="utf-8") as file:
    for line in lines:
        if line.strip() != line_to_remove:
           file.write(line)


print("✅ DAST report generated and saved to dast_report.txt.")                                                                                                                                        1,1           Top
