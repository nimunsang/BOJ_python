#해결 #브루트포스알고리즘 #백트래킹
"""
https://www.acmicpc.net/problem/14889
[14889] : 스타트와 링크
"""

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

c = combinations(range(N), N//2)
total_comb = list(map(list, c))
rang = list(range(N))

min_result = 1000000

for lst in total_comb:
    sum_lst = 0
    sum_rest_lst = 0
    rest_lst = list(set(rang) - set(lst))
    c = combinations(lst, 2)
    comb = list(map(list, c))
    for i in comb:
        sum_lst += arr[i[0]][i[1]] + arr[i[1]][i[0]]

    c = combinations(rest_lst, 2)
    comb = list(map(list, c))
    for i in comb:
        sum_rest_lst += arr[i[0]][i[1]] + arr[i[1]][i[0]]
    
    result = abs(sum_lst - sum_rest_lst) 
    if result < min_result:
        min_result = result

print(min_result)