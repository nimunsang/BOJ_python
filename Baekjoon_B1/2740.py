N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

B = []
M, K = map(int, input().split())
for i in range(M):
    B.append(list(map(int, input().split())))

for i in range(N):  
    for p in range(K):
        s = 0
        for j in range(M): 
            s += A[i][j]*B[j][p]
        print(s, end = " ")     
    print()