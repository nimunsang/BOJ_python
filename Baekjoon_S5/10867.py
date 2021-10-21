"""
https://www.acmicpc.net/problem/10867
[10867] : 중복 빼고 정렬하기
"""

N = int(input())

lst = list(map(int, input().split()))

lst = list(set(lst))

for i in sorted(lst):
    print(i, end = " ")