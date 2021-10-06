N = int(input())
lst = list(map(int, input().split()))

res = [1]
cnt = 1
for i in range(1, N):
    cnt += 1
    res.insert(lst[i], cnt)

res.reverse()
for i in res:
    print(i, end = " ")