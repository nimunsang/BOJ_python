#30분 #정렬
"""
https://www.acmicpc.net/problem/10825
[10825] : 국영수
"""
import sys
input = sys.stdin.readline

N = int(input())

student_lst = []
for i in range(N):
    lst = list(map(str, input().split()))
    student_lst.append((lst[0], int(lst[1]), \
        int(lst[2]), int(lst[3])))

student_lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(student_lst[i][0])