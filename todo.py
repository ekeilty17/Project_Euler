import os

all_files = os.listdir('.')
python_scripts = [script for script in all_files if os.path.splitext(script)[1] == ".py" and script != "todo.py"]

incomplete = [False] * 1000
completed = [False] * 1000
for script in python_scripts:
    if script[0] == "_":
        n = script[2:5]
        incomplete[int(n)-1] = True
    else:
        n = script[1:4]
        completed[int(n)-1] = True

print("Started but not finished problems:")
for i, prob in enumerate(incomplete, 1):
    if prob:
        print(i)

Total = 20
print(f"\nNext {Total} Unstarted Problems")

cnt = 0
for i, prob in enumerate(completed, 1):
    if not prob:
        print(i)
        cnt += 1
    if cnt > Total:
        break