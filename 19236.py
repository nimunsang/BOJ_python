from copy import deepcopy

arr = [[[0, 0] for _ in range(4)] for _ in range(4)]
inp = [list(map(int, input().split())) for _ in range(4)]
fishes = [[0, 0, 0] for _ in range(17)]

for i in range(4):
    for j in range(8):
        if j%2 == 0:
            fishnumber = inp[i][j]
            arr[i][j//2][0] = fishnumber
            fishes[fishnumber][0], fishes[fishnumber][1] = i, j//2
        else:
            fishdirection = inp[i][j]-1
            arr[i][j//2][1] = fishdirection
            fishes[fishnumber][2] = fishdirection


def fishmove(shk, fishlist, arr):  # 클리어
    moved_arr = deepcopy(arr)
    for i in range(1, 17):
        if i not in fishlist:
            cnt = 0
            y, x, dir = fishes[i]
            while cnt < 8:
                next_dir = (dir+cnt) % 8
                ny, nx = y + direction[next_dir][0], x + direction[next_dir][1]

                if 0 <= ny < 4 and 0 <= nx < 4 and shk != [ny, nx]:
                    targetfishnumber, targetfishdirection = arr[ny][nx]
                    arr[y][x][1] = next_dir
                    fishes[i][2] = next_dir
                    arr[y][x], arr[ny][nx] = arr[ny][nx], arr[y][x]  # swap

                    fishes[i][0], fishes[i][1] = ny, nx  # fish의 정보를 서로 교환
                    fishes[targetfishnumber][0], fishes[targetfishnumber][1]= y, x
                    break

                else:
                    cnt += 1
    return moved_arr


def dfs(y, x, fishlist, arr):
    global answer

    fishdirection = arr[y][x][1]
    dy, dx = direction[fishdirection]

    # 상어의 움직임
    for i in range(1, 4):
        visited = 0
        sy, sx = y + dy*i, x + dx*i
        if 0 <= sy < 4 and 0 <= sx < 4 and arr[sy][sx][0] not in fishlist:
            nextfish = arr[sy][sx][0]
            visited = 1
            moved_arr = fishmove([sy, sx], fishlist + [nextfish], arr)
            dfs(sy, sx, fishlist + [nextfish], moved_arr)

    if visited == 0:
        print(fishlist)
        answer = max(answer, sum(fishlist))
        return


answer = 0
shark = [0, 0]
firstfishnumber = arr[0][0][0]
direction = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
arr = fishmove([0, 0], [firstfishnumber], arr)
dfs(0, 0, [firstfishnumber], arr)
print(answer)