#1시간 #구현 #시뮬레이션
"""
https://www.acmicpc.net/problem/20055
[20055] : 컨베이어 벨트 위의 로봇
"""

N, K = map(int, input().split())
inp = list(map(int, input().split()))
up, down = inp[:N], inp[N:][::-1]
arr = [up, down]
robot = [0] * N


def rotate_arr(a):
    upp = [a[1][0], a[0][0]]
    for i in range(1, N-1):
        upp.append(a[0][i])

    downn = []
    for i in range(1, N-1):
        downn.append(a[1][i])
    downn.append(a[1][-1])
    downn.append(a[0][-1])

    return [upp, downn]


answer = 1
while True:
    arr = rotate_arr(arr)
    robot = [0] + robot[:-1]
    if robot[-1]:
        robot[-1] = 0

    for i in range(N-2, -1, -1):
        if robot[i] and not robot[i+1] and arr[0][i+1]:
            if i+1 == N-1:
                robot[i+1] = 0
            else:
                robot[i+1] = 1
            robot[i] = 0
            arr[0][i+1] -= 1

    if arr[0][0]:
        robot[0] = 1
        arr[0][0] -= 1

    if sum(map(lambda x: x.count(0), arr)) >= K:
        break

    answer += 1

print(answer)
