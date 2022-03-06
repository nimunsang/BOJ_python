# https://www.acmicpc.net/problem/10942

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ispalindrome = [[0] * N for _ in range(N)]

for length in range(N):
    if length == 0:  # 길이가 1인 놈들은 모두 palindrome이다.
        for i in range(N):
            ispalindrome[i][i] = 1

    elif length == 1:  # 길이가 2인 놈들은 두 글자가 같으면 palindrome이다.
        for i in range(N-1):
            if arr[i] == arr[i+1]:
                ispalindrome[i][i+1] = 1

    else:  # 길이가 3 이상인 놈들은 가운데가 palindrome이고, 양 끝의 글자가 같으면 palindrome이다.
        for i in range(N-length):
            if ispalindrome[i+1][i+length-1] == 1 and arr[i] == arr[i+length]:
                ispalindrome[i][i+length] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(ispalindrome[S-1][E-1])
