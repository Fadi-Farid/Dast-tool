import requests
import os
import re

Token = os.getenv("GITHUB_TOKEN")
def RaisePR(GITHUB_TOKEN):

    headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "title": "AI Fix for the issue",
        "body": "This PR implements the authentication feature using AIOps",
        "head": "issue-fix",
        "base": "main"
    }

    response = requests.post("https://api.github.com/repos/Fadi-Farid/python-web-app/pulls", headers=headers, json=data)

    if response.status_code == 201:
        print("Pull request created successfully.")
    else:
        print(f"Failed to create pull request. Status code: {response.status_code}")
        print(response.json())
        print("Response content:", response.text)

def main():
  
                def list_github_files(owner, repo):
                    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/"
                    response = requests.get(api_url)
                    if response.status_code == 200:
                        files = [item['name'] for item in response.json()]
                        return files
                    else:
                        print("Failed to fetch repository contents.")
                        return []
                
                # Example usage
                files = list_github_files("Fadi-Farid", "Dast-tool")
                print(files)
                
                
                with open('dast_report.txt', 'r', encoding='utf-8') as file:
                     content = file.read()
                
                # Split the content into words
                words = content.split()
                
                # Find matches
                matched_files = [file_name for file_name in files if file_name in words]
                print("Matched file names:", matched_files)
                
                
                
                # Define common file extensions
                file_extensions = ['.py', '.html', '.css', '.js', '.json', '.txt', '.md', '.xml', '.yml', '.yaml']
                
                # Read the content of the file
                with open('dast_report.txt', 'r', encoding='utf-8') as file:
                  content = file.read()
                
                # Build regex pattern to match file names
                pattern = r'\b[\w\-]+\.(?:' + '|'.join(ext.strip('.') for ext in file_extensions) + r')\b'
                
                # Find all matching file names
                matched_files = re.findall(pattern, content)
                
                # Output the results
                print("Extracted file names from dast_report.txt:")
                for file_name in matched_files:
                    print(file_name)
                
                end_marker = "```"
                start_marker = file_name
                started = "```python"
                starting = False
                copying = False
                extracted_lines = []
            
                with open("dast_report.txt", "r", encoding="utf-8") as file:
                    for line in file:
                        if end_marker in line  and starting:
                            break
                        if start_marker in line:
                           copying = True
                        if  starting:
                            extracted_lines.append(line)
                        if started in line:
                            starting = True
                        # Output the result
                print("".join(extracted_lines))
                with open(file_name, "w") as f:
                    for entry in extracted_lines:
                        f.write(entry)

                command=(f'git clone https://{Token}@github.com/Fadi-Farid/python-web-app.git')
                os.system(command)
                command=("git init && \
                git checkout -b issue-fix && \
                cp -f file_name . && \
                git add . && git commit -m 'Fix Commit' &&\
                git push https://{Token}@github.com/Fadi-Farid/python-web-app.git issue-fix")
                os.system(command)   

                print(Token)
                RaisePR(Token)

if __name__ == "__main__":
    main()
