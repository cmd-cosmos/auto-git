#pylint: skip-file

import requests

def fetch_repo_list(username):
    '''
    Fetches list of repos and privacy status from gh api.
    
    :param username: github username
    '''
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, timeout=5)
    if response.status_code == 404:
        print()
        print("#### Invalid User")
        print()
        return
    else:
        repos = response.json()
        # print(repos)
        for repo in repos:
            print(f"Repo: {repo["name"]:50} | Private: {repo["private"]}")

