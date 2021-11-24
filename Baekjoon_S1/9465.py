#다시 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/9465
[9465] : 스티커
"""
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    line = [list(map(int, input().split())) for _ in range(2)]


    for i in range(1, N):
        if i == 1:
            line[1][1] = line[1][1] + line[0][0]
            line[0][1] = line[0][1] + line[1][0]
            
        else:
            line[0][i] = max(line[1][i-1] + line[0][i], line[1][i-2] + line[0][i])
            line[1][i] = max(line[0][i-1] + line[1][i], line[0][i-2] + line[1][i])

    print(max(line[0][N-1], line[1][N-1]))