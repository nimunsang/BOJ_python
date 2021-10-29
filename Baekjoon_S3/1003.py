#20분 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/1003
[1003] : 피보나치 함수
"""

def sol(n):
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        arr = [0] * 41
        arr[0] = 1
        arr[1] = 1
        for i in range(2, n+1):
            arr[i] = arr[i-1] + arr[i-2]
        
        return [arr[n-2], arr[n-1]]


T = int(input())
for i in range(T):
    N = int(input())
    print(' '.join([str(i) for i in sol(N)]))