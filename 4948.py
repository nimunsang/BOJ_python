#25분 #수학 #정수론 #소수판정 #에라토스테네스의체
"""
https://www.acmicpc.net/problem/4948
[4948] : 베르트랑 공준
"""

lst = []
visited = [0] * (123456*2+1)
for i in range(2, 123456*2+1):
    if visited[i] == 0:
        lst.append(i)
        for j in range(i, 2*123456+1, i):
            visited[j] = 1


while True:
    n = int(input())
    if n == 0:
        break

    else:
        cnt = 0
        for i in lst:
            if n<i<=2*n:
                cnt += 1
        print(cnt)
