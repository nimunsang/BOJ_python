N, M = map(int, input().split())

A = []
B = []
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]
        print(A[i][j], end = " ")
    print("")