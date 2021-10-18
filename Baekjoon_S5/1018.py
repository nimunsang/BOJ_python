N, M = map(int, input().split())
lst = []
for i in range(N):
    lst.append(input())


mask = [[0]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
            if lst[i][j] == "B": mask[i][j] = 1
        elif (i%2 == 1 and j%2 == 0) or (i%2 == 0 and j%2 == 1):
            if lst[i][j] == "W": mask[i][j] = 1

s_lst = []
a, b = 0, 0
while True:
    s = 0
    for i in range(a, a+8):
        for j in range(b, b+8):
            s += mask[i][j]
    s_lst.append(s)
    
    b += 1
    if b == M-7:
        a += 1
        b = 0
    if a == N-7: break

print(min(min(s_lst), 64 - max(s_lst)))