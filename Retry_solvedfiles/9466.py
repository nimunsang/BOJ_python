# https://www.acmicpc.net/problem/9466

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def find_team(student):
    global made_team

    team.append(student)
    visited[student] = 1
    next_student = students[student]

    if visited[next_student]:
        if next_student in team:
            made_team += team[team.index(next_student):]
            return

    else:
        find_team(next_student)


T = int(input())

for _ in range(T):
    N = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [0] * (N+1)
    made_team = []
    for i in range(1, N+1):
        if not visited[i]:
            team = []
            find_team(i)

    print(N - len(made_team))
