"""
https://www.acmicpc.net/problem/1065
[1065] : 한수
"""

N = int(input())

cnt = 0
for i in range(1, N+1):
    i = str(i)
    if len(i) <= 2:
        cnt += 1
    else:
        d = int(i[1]) - int(i[0])
        mask = 1
        for j in range(len(i)-1):
            if int(i[j+1]) - int(i[j]) != d:
                mask = 0
                break
        if mask == 1:
            cnt += 1

print(cnt)