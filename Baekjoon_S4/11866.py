# 6분.. 실5에서 풀었던 문제여서 쉽게 풀었다
# 앞서 배운 deque을 사용하면 더 쉬울것 같아서
# deque도 써보았다.
"""
https://www.acmicpc.net/problem/11866
[11866] : 요세푸스 문제0
"""

from collections import *

N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]
lst = deque(lst)

new_lst = []
for i in range(N):
    lst.rotate(-K)
    new_lst.append(lst.pop())

print(f"<{', '.join([str(i) for i in new_lst])}>")


# N, K = map(int, input().split())

# lst = [i for i in range(1, N+1)]

# ind = K-1

# new_lst = []
# for i in range(N):
#     if ind >= len(lst):
#         ind = ind%len(lst)
#     new_lst.append(lst.pop(ind))
#     ind += K-1

# print(f"<{', '.join([str(i) for i in new_lst])}>")