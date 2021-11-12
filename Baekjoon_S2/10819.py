#40분 #브루트포스알고리즘 #백트래킹
"""
https://www.acmicpc.net/problem/10819
[10819] : 차이를 최대로
"""

from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

"""
짝수일때 효율적으로 구하는거는 알겠는데
홀수를 잘 모르겠어서 그냥 permutations 썼다
"""
# A.sort()
# lst = [0] * N
# if N % 2 == 0:
#     for i in range(1, N//2+1):
#         if i % 2 == 0:
#             lst[N//2-i] = A.pop(0)
#             lst[N//2+(i-1)] = A.pop(-1)
#         else:
#             lst[N//2-i] = A.pop(-1)
#             lst[N//2+(i-1)] = A.pop(0)
    
#     res = 0
#     for i in range(N-1):
#         res += abs(lst[i] - lst[i+1])
#     print(res)

# else:
max_c = 0
c = permutations(A, N)
for i in c:
    s = 0 
    for a in range(N-1):
        s += abs(i[a] - i[a+1])
    if s > max_c:
        max_c = s

print(max_c)