N = int(input())
X = list(map(int, input().split()))

cnt = 0
for i in range(5):
    if(N == X[i]):
        cnt += 1
print(cnt)