#다시 #자료구조 #분리집합
"""
https://www.acmicpc.net/problem/1717
[1717] : 집합의 표현
"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
root = [i for i in range(n+1)]

def find(x):
    if root[x] == x:
        return x
    
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        root[x] = y

for i in range(m):
    mask, a, b = map(int, input().split())
    if mask == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)