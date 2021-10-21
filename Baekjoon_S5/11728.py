"""
https://www.acmicpc.net/problem/11728
[11728: 배열 합치기]
"""
N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in sorted(A+B):
    print(i, end = " ")