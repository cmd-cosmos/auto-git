#pylint: skip-file

# isolated testing env for functions being worked on.


op_dict = {
        0 : "default routine",
        1 : "status check",
        2 : "branch ops",
        3 : "stage changes",
        4 : "commit changes",
        5 : "push changes",
    }
print("Auto Git Sequence Menu:\n")
print("*"*70)
print("id |     operation")
print("----------------------")
for key,val in op_dict.items():
    print(f"{key}  | {val}")
print("*"*70)
print()
print("ALERT: invalid input will result in fallback to default routine.\n")
input("Enter op id: ")