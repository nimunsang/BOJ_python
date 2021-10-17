s = input()

lst = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in lst:
    s = s.replace(i, "_")

print(len(s))