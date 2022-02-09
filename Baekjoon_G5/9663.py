#해결 #브루트포스알고리즘 #백트래킹
"""
https://www.acmicpc.net/problem/9663
[9663] : N-Queen
"""

N = int(input())
arr = [0 for _ in range(N)]
res = 0 

def check(n):
    for i in range(n):
        if arr[n] == arr[i] or n-i == abs(arr[n] - arr[i]):
            return False
    
    return True

def solve(n):
    global res
    if n == N:
        res += 1
        return
    
    for i in range(N):
        arr[n] = i
        if check(n):
            solve(n+1)

solve(0)
print(res)