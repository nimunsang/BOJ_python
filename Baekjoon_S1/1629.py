#다시 #수학 #분할정복을이용한거듭제곱
"""
https://www.acmicpc.net/problem/1629
[1629] : 곱셈
"""

A, B, C = map(int, input().split())

def solve(a, b):
    if b == 1:
        return a%C
    
    tmp = solve(a, b//2)

    if b%2 == 0:
        return tmp*tmp%C
    else:
        return tmp*tmp*a%C

print(solve(A, B))

#print(pow(A, B, C))