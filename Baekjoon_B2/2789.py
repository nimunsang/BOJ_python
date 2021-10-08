s = input()
mask = "CAMBRIDGE"

for i in s:
    if not(i in mask):
        print(i, end = "")