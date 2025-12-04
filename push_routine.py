#pylint: skip-file
#type: ignore

import subprocess
import os
import time

def menu_push_routine():

    branch = subprocess.check_output(
        ["git", "branch", "--show-current"], text=True
    ).strip()

    res = subprocess.run(
        ["git", "log", f"origin/{branch}..HEAD", "--oneline"], capture_output=True, text=True
    )

    if res.stdout:
        print("Commit History:")
        print(res.stdout)
        remote_check = os.system("git remote -v")
        if remote_check == 0: 
            os.system("git push")
        else:
            print("Remote does not exist.")

menu_push_routine()
