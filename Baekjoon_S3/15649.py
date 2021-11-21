#해결 #백트래킹
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

"""
내가 나중에 다시 푼 풀이

N, M = map(int, input().split())

visited = [0] * (N+1)
lst = []
def solve(n , depth):
    global visited
    if depth == M:
        print(*lst)
        return

    for i in range(1, n+1):
        if visited[i] == 0:
            lst.append(i)
            visited[i] = 1
            depth += 1
            solve(n, depth)

            depth -= 1
            visited[i] = 0
            lst.pop()

solve(N, 0)
"""
"""
from itertools import permutations

N, M = map(int, input().split())
p = permutations(range(1, N+1), M)

for i in p:
    print(*i)
"""