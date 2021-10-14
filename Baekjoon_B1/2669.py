lst = []
for i in range(4):
    lst.append(list(map(int, input().split())))

maxlst = 0
for i in range(4):
    if max(lst[i]) > maxlst: maxlst = max(lst[i])

xylst = [[0] *maxlst for _ in range(maxlst)] # 8*8

for i in range(4):
    
    for a in range(lst[i][0], lst[i][2]):
        for b in range(lst[i][1], lst[i][3]):
            xylst[a][b] = 1

s = 0
for i in range(maxlst):
    s += sum(xylst[i])
print(s)