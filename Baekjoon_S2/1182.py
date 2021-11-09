#20분 #브루트포스알고리즘
"""
https://www.acmicpc.net/problem/1182
[1182] : 부분수열의 합
"""

from itertools import combinations

N, S = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):
    c = combinations(lst, i)
    for j in c:
        if sum(j) == S:
            cnt += 1

print(cnt)