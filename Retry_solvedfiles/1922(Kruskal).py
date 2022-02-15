"""
https://www.acmicpc.net/problem/1922
"""

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    parent[a] = b


N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

graph.sort(key=lambda x: x[2])

answer = 0
for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)
