#1시간반 #구현 #브루트포스알고리즘
"""
https://www.acmicpc.net/problem/3085
[3085] : 사탕 게임
"""

import sys
input = sys.stdin.readline

N = int(input())

def trans(arr, n):
    new_arr = [[""]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = arr[j][i]
    return new_arr

arr = []
for i in range(N):
    arr.append(list(input().rstrip()))


max_count_lst = []
for a in range(N):
    row_max_count = []
    for i in range(N-1):
        max_count = 1
        trans_max_count = 1
        copy_arr = arr
        trans_copy_arr = trans(copy_arr, N)
        if copy_arr[a][i] != copy_arr[a][i+1]:
            copy_arr[a][i], copy_arr[a][i+1]\
            = arr[a][i+1], arr[a][i]
            
            cnt = 1
            trans_cnt = 1
            trans_copy_arr = trans(copy_arr, N)
            for j in range(N-1):
                if copy_arr[a][j] == copy_arr[a][j+1]:
                    cnt += 1
                    if cnt > max_count:
                        max_count = cnt
                else:
                    cnt = 1

                if trans_copy_arr[a][j] == trans_copy_arr[a][j+1]:
                    trans_cnt += 1
                    if trans_cnt > trans_max_count:
                        trans_max_count = trans_cnt
                else:
                    trans_cnt = 1

        copy_arr[a][i], copy_arr[a][i+1]\
        = arr[a][i+1], arr[a][i]

        trans_copy_arr[a][i], trans_copy_arr[a][i+1]\
        = arr[a][i+1], arr[a][i]

        row_max_count.append(max_count)
        row_max_count.append(trans_max_count)
    max_count_lst.append(max(row_max_count))

    if len(set(arr[a])) == 1:
        max_count_lst[a] = N
                    
print(max(max_count_lst))