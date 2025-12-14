#pylint: skip-file

# isolated testing env for functions being worked on.

import requests

def menu_test():
    op_dict = {
            0 : "default routine",
            1 : "status check",
            2 : "branch ops",
            3 : "stage changes",
            4 : "commit changes",
            5 : "push changes",
        }

    op_msgs = [
    "executing default routine",
    "fetching current branch status",
    "loading bracnch ops selection menu",
    "proceeding with staging operation",
    "proceeding with commit sequence for staged changes",
    "pushing commited changes to remote"]

    print("Auto Git Sequence Menu:\n")
    print("*"*70)
    print("id |     operation")
    print("----------------------")
    for key,val in op_dict.items():
        print(f"{key}  | {val}")
    print("*"*70)
    print()
    print("ALERT: invalid input will result in fallback to default routine.\n")
    try:
        menu_selection = int(input("Enter op id: "))
    except ValueError:
        print()
        print("*"*70)
        print("invalid input...")
        print("fallback to default routine.")
        menu_selection = 0
        print()
    if menu_selection not in op_dict.keys():
        print("*"*70)
        print("INVALID OP ID: RANGE ERROR")
        print("fallback to default routine")
        print("*"*70)
    else: 
        print(f"setting op id: {menu_selection}")
        print(op_msgs[menu_selection])
        print("*"*70)

def fetch_repo_list(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, timeout=5)
    if response.status_code == 404:
        print("Invalid User")
        return
    else:
        repos = response.json()
        # print(repos)
        for repo in repos:
            print(f"Repo: {repo["name"]:50} | Private: {repo["private"]}")

if __name__ == "__main__":
    # menu_test()
    username = input("Enter User Name: ").strip()
    fetch_repo_list(username=username)