arr = [[1, 1, 1], [0 ,0 ,0], [2, 2, 2]]

print(list(zip(*arr[::-1])))

for a in arr:
    print(*a)

for a in list(zip(*arr[::-1])):
    print(*a)

print(*arr[::-1])