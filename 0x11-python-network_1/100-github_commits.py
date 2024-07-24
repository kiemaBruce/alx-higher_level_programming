#!/usr/bin/python3
"""Shows commits into a repository by a specific user"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    r = requests.get(url)
    if r.status_code == 200:
        commits_list = r.json()
        formatted_commits = []
        i = 0
        for commit in commits_list:
            if i == 10:
                break
            commit_str = ""
            commit_str += commit.get('sha')
            commit_str += ': '
            commit_str += commit.get('commit').get('author').get('name')
            formatted_commits.append(commit_str)
            i += 1
        for item in formatted_commits:
            print(item)
    else:
        print(None)
