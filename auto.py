# purpose:
# git status
# git add
# git commit

# type: ignore
# pylint ignores ---> ignore globals whitespace in multiline function calls
# pylint: disable=global-statement
# pylint: disable=C0303
# pylint: disable=C0301
# pylint: disable=C0114

import time
import os
import sys
import subprocess
from art import bat2, bat3

print(bat2)

# init global vars to none
STATUS = None
CHANGES_FLAG = None

def git_root_getter(start=None):
    ''' get git root '''
    try:
        res = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, cwd=start, check=True)
        return res.stdout.strip() 
    except subprocess.CalledProcessError:
        print("Not a git repo")
        sys.exit()

if len(sys.argv) > 1:
    target_path = sys.argv[1]
    print(f"target set: {target_path}\n")
else:
    target_path = os.getcwd()
    print("no target dir passed, using program home dir...\n")
    print(f"target set: {target_path}")

git_root = git_root_getter(target_path)
print(f"git root established: {git_root}")
os.chdir(git_root)

print("-"*30, "Auto Git", "-"*30, '\n')

CHANGES_FLAG = False

def validate_and_status_check():
    '''
    validation sequence to ensure git repo exists before checking for repo status.
    '''
    check = os.system("git rev-parse --git-dir")
    print("git repo check returned: ",check)

    if check == 0:
        print(".git directory confirmed, proceeding with auto commit sequence.\n")
        print("-"*70)
    else:
        print("not a git directory")
        print("-"*70)

    time.sleep(2)
    global STATUS #ignore : warning
    STATUS = os.system("git status")
    print("-"*70)
    print("status check return val: ", STATUS)

    command = subprocess.run(["git", "status", "--porcelain"],
                                  capture_output=True, text=True, check=False)   

    if bool(command.stdout.strip()) is True:
        time.sleep(1)
        print("changes found.")
        print("proceeding with the auto track sequence.")
        global CHANGES_FLAG
        CHANGES_FLAG = not CHANGES_FLAG
    else:
        time.sleep(1)
        print("no changes found.\n---> exiting sequence...\n")
        time.sleep(1)
        sys.exit()

def modified_file_getter():
    '''
    get list of modified files after a git status check
    '''
    change_check = subprocess.run(["git", "status", "--porcelain"],
                                  capture_output=True, text=True, check=False)    
    file_tracker = change_check.stdout

    file_tracker_lst = file_tracker.split('\n')
    
    if '' in file_tracker_lst:
        file_tracker_lst.remove('')
    # print(file_tracker_lst)
    
    # strip the path if called other files from separate directory
    splitter = [os.path.abspath(member[2:].strip()) for member in file_tracker_lst]
    # print(splitter)

    print(f"Changed files:\n{file_tracker}")
    print("-"*70)
    print("idx : filename\n")
    for i,mod_file in enumerate(splitter):
        print(f"{i} : {mod_file.rstrip()}")
    print()

    file_inp = int(input("enter index of file to stage: "))
    if file_inp in range(len(splitter)):
        print(f"selecting: {splitter[file_inp]}")
        os.system(f"git add {splitter[file_inp]}")
        commit(add_mode=2)
    else:
        print("index out of range...")
        sys.exit()

validate_and_status_check()
print("-"*70)
print(f"validation and status bit: {CHANGES_FLAG}") 
print("-"*70)

MODE = 1 # 0 = debug mode, 1 = run mode
if MODE and CHANGES_FLAG:
    PROCEED = False

    def check_remote_and_push():
        '''
        check if remote exists and push if remote found
        '''

        print("\nchecking if remote exists for the current git repo.")
        time.sleep(1)
        remote_check = os.system("git remote -v")
        print("remote check: ", remote_check)
        if remote_check == 0:
            print("remote found...")
            print("pushing to remote...\n")
            time.sleep(1)
            os.system("git push")
            time.sleep(1)
            print("-"*70)
            print("\ngetting branch status...")
            time.sleep(1)
            os.system("git status")
            time.sleep(1)
            print("-"*70)

            clean_flag = input("would you like to clear screen[y/n]: ").lower().strip()
            if clean_flag == 'y':
                print("clearing screen...")
                print("look at this cool artwork in the meantime...")
                print(bat3)
                print("I am Vengeance...")
                time.sleep(1)
                print("I am the Night...")
                time.sleep(1)
                print("I am Batman...")
                time.sleep(4)
                os.system("cls")
            elif clean_flag == 'n':
                art_flag = input("would you like to look at some cool art[y/n]: ").lower().strip()
                if art_flag == 'y':
                    print("\n"*100)
                    print("I am Vengeance")
                    time.sleep(1)
                    print("I am the Night")
                    time.sleep(1)
                    print("I am Batman")
                    time.sleep(1)
                    print(bat3)
                    time.sleep(1)
                    sys.exit()
                else:
                    print("\nsequence complete...\n")
                    time.sleep(1)
                    print("I am Vengeance")
                    time.sleep(1)
                    print("I am the Night")
                    time.sleep(1)
                    print("I am Batman")
                    time.sleep(1)
                    print(bat3)
        else:
            print("no remote found...")
            print("exiting sequence without pushing to remote....")
            time.sleep(1)
            sys.exit()

    def commit(add_mode):
        '''
        proceed with git commit sequence after git add returns and user passes custom message 
        otherwise goes with the default version
        '''
        if add_mode == 1:
            os.system("git add --all")
        elif add_mode == 2:
            pass
        print("\nFetching status...")
        os.system("git status")
        print("-"*70)
        inp_flag = input("Add custom message for the commit[y/n]: ").lower().strip()
        print()

        if inp_flag == 'y':
            msg_string = input("Enter custom message: ").strip()
            print(f"Message String: {msg_string}")
            time.sleep(2)
        elif inp_flag == 'n':
            ### add a list of default strings and prompt user to choose default message else push the system defualt message.
            msg_list = [
                "Initial commit.",
                "Updated README.md",
                "No major changes made.",
                "Minor formatting changes.",
                "Temporary commit.",
                "Modified comments.",
                "Cleanup.",
                "Auto Commit Sequence --> system default message",
            ]
            n = len(msg_list)
            n_div = n // 2
            left = msg_list[:n_div]
            right = msg_list[n_div:]

            for i,(l,r) in enumerate(zip(left,right)):
                l_idx = i
                r_idx = i + n_div
                print(f"{l_idx:>2}: {l:<40} {r_idx:>2}: {r}")

            msg_choice = int(input("Enter default messag idx: "))
            print(f"Default Commit Message Choice: {msg_choice}\n")
            def_choice = -1 # add user input logic block
            chosen_idx = def_choice if (inp_flag not in ('y', 'n')) else msg_choice
            msg_string = msg_list[chosen_idx]
            print(f"Commit Message String: {msg_string}")

        print()
        os.system(f'git commit -m "{msg_string}"')
        time.sleep(2)
        print("-"*70)
        push_conf = input("ready to push changes[y/n]: ").lower().strip()
        if push_conf == "y":
            check_remote_and_push()
        else:
            print("\nexiting without pushing.")
            time.sleep(1)
            sys.exit()

    if STATUS == 0:
        print("status check successful --> proceeding with git add sequence")
        print(f"cwd: {os.getcwd()}")
        print("\nconfirm add permission to stage all modified files in the cwd.")
        inp = input("confirm git add --all [y/n]: ")
        if inp == 'y':
            PROCEED = True
            print("\nproceeding to auto commit sequence...")
            commit(add_mode=1)
        elif inp == "n":
            specific_inp = input("would you like to add specific files[y/n]: ")
            if specific_inp == "y":
                print("Select index of file you want to add...")
                modified_file_getter()
            else:
                PROCEED = False
                print("-"*70)
                print("terminating process ---> exiting seq.")
                time.sleep(1)
                print("I am Vengeance")
                time.sleep(1)
                print("I am the Night")
                time.sleep(1)
                print("I am Batman")
                time.sleep(1)
                print(bat3)
                time.sleep(3)
                sys.exit()
    else:
        print("failure --> exiting")
        sys.exit()
