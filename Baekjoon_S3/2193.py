#10분 #다이나믹프로그래밍
"""
https://www.acmicpc.net/problem/2193
[2193 : 이친수]
"""
N = int(input())
arr = [0, 1, 1]
if N >= 3:
    for i in range(3, N+1):
        arr.append(arr[i-1] + arr[i-2])

print(arr[N])