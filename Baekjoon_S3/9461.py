#20분 #수학 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/9461
[9461] : 파도반 수열
"""

T = int(input())

lst = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(10, 101):
    lst.append(lst[i] + lst[i-4])

for i in range(T):
    n = int(input())
    print(lst[n])