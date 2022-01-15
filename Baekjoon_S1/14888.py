#해결 #40분 #브루트포스알고리즘 #백트래킹
"""
https://www.acmicpc.net/problem/14888
[14888] : 연산자 끼워넣기
"""

import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
oper = list(map(int, input().split()))
op_lst = ['+', '-', '*', '/']

operlst = []
for i in range(4):
    for j in range(oper[i]):
        operlst.append(op_lst[i])

minimum = 1e9
maximum = -1e9

"""
permutation을 활용하여 푼 방법(1)
"""
# def calculate(n, oplst):
#     global minimum, maximum
#     p = permutations(oplst, n-1)
#     for permutation_lst in p:
#         res = A[0]
#         ind = 1
#         for i in permutation_lst:
#             if i == '+':
#                 res += A[ind]
#             elif i == '-':
#                 res -= A[ind]
#             elif i == '*':
#                 res *= A[ind]
#             else:
#                 res = int(res / A[ind])
#             ind += 1
        
#         if res < minimum :
#             minimum = res
#         if res > maximum :
#             maximum = res

# calculate(N, operlst)
# print(maximum)
# print(minimum)

"""
dfs를 활용하여 푼 방법(2)
훨씬 빠르다
"""
def dfs(depth, total, plus, minus, mult, div):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if plus:
        dfs(depth+1, total+A[depth], plus-1, minus, mult, div)
    if minus:
        dfs(depth+1, total-A[depth], plus, minus-1, mult, div)
    if mult:
        dfs(depth+1, total*A[depth], plus, minus, mult-1, div)
    if div:
        dfs(depth+1, int(total / A[depth]), plus, minus, mult, div-1)

dfs(1, A[0], oper[0], oper[1], oper[2], oper[3])
print(maximum)
print(minimum)