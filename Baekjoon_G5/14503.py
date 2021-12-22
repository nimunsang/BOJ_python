#1시간 #구현 #시뮬레이션
"""
https://www.acmicpc.net/problem/14503
[14503] : 로봇 청소기
"""

def input():
    import sys
    input = sys.stdin.readline

    global N, M, r, c, d, arr
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

# dx[d], dy[d] = [북, 동, 남, 서] 
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def move(y, x):
    from collections import deque
    global d, answer

    q = deque([])
    q.append([y, x])
    arr[y][x] = 2

    while q:
        v = q.popleft()
        cnt = 0
        back = False
        while True:
            if d == 0:
                d = 4
            d -= 1
            
            if arr[dy[d]+v[0]][dx[d]+v[1]] == 0:
                break

            cnt += 1
            if cnt == 4:
                if arr[v[0]-dy[d]][v[1]-dx[d]] == 1:
                    return
                
                else:
                    q.append([v[0]-dy[d], v[1]-dx[d]])
                    back = True
                    break
        
        if back == False:
            q.append([dy[d]+v[0], dx[d]+v[1]])
            arr[dy[d]+v[0]][dx[d]+v[1]] = 2
            answer += 1
            
input()
answer = 1
move(r, c)
print(answer)