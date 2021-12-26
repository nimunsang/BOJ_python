#구현 #브루트포스알고리즘
"""
https://www.acmicpc.net/problem/15686
[15686] : 치킨 배달
"""

from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append([i, j])
        elif city[i][j] == 2:
            chickens.append([i, j])

comb = combinations(chickens, M)
mind = 100000
for c in comb:
    s = 0
    for house in houses:
        d = []
        for chicken in c:
            d.append(abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))
        s += min(d)
        if s >= mind:
            break
    
    if s < mind:
        mind = s
        
print(mind)