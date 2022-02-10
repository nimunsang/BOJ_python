#해결 #자료구조 #스택
"""
https://www.acmicpc.net/problem/17298
[17298] : 오큰수
"""
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

ans = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)

print(*ans)