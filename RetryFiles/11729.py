#다시 #재귀
"""
https://www.acmicpc.net/problem/11729
[11729] : 하노이 탑 이동 순서
"""

N = int(input())

def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
    
    else:
        hanoi(n-1, start, end, mid)
        print(start, end)
        hanoi(n-1, mid, start, end)

print(2**N - 1)
hanoi(N, 1, 2, 3)