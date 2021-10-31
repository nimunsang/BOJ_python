#다시 #백트래킹
"""
https://www.acmicpc.net/problem/15649
[15649] : N과 M(1)
백트래킹을 처음 접한 문제다.
오랜 시간 고민했고, 해답을 찾아보았다.
순열 관련 stl이 있다는 것도 확인했다.
"""

N, M = map(int, input().split())

lst = []

def dfs():
    if len(lst) == M:
        print(' '.join(map(str, lst)))
        return
    
    else:
        for i in range(1, N+1):
            if i not in lst:
                lst.append(i)
                dfs()
                lst.pop()

dfs()


# from itertools import permutations

# N, M = map(int, input().split())

# p = permutations(range(1, N+1), M)
# for i in p:
#     print(' '.join(map(str, i)))





