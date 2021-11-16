#30분 #다이나믹프로그래밍 #재귀
"""
https://www.acmicpc.net/problem/9184
[9184] : 신나는 함수 실행
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dp = [[[0]*21 for i in range(21)] for j in range(21)]

def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20, 20, 20)
    
    #값이 이미 존재한다면 그 값을 바로 리턴한다.
    if dp[a][b][c]:
        return dp[a][b][c]
    
    #메모이제이션... dp[a][b][c]를 계속 기록
    if a<b<c:
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return dp[a][b][c]
    
    dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())

    if a==-1 and b==-1 and c==-1:
        break

    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")




# =====내 풀이.. 20**3 을 다 구해놓고 푸는 방법이었다.
# lst = [[[1]*21 for i in range(21)] for j in range(21)]
# for a in range(1, 21):
#     for b in range(1, 21):
#         for c in range(1, 21):
#             if a < b < c:
#                 lst[a][b][c] = lst[a][b][c-1] + lst[a][b-1][c-1] - lst[a][b-1][c]

#             else:
#                 lst[a][b][c] = lst[a-1][b][c] + lst[a-1][b-1][c] \
#                     + lst[a-1][b][c-1] - lst[a-1][b-1][c-1]
# while True:
#     a, b, c = map(int, input().split())
#     if (a, b, c) == (-1, -1, -1):
#         break

#     else:
#         if a<=0 or b<=0 or c<=0 :
#             res = 1

#         elif a > 20 or b > 20 or c > 20:
#             res = lst[20][20][20]
        
#         else:
#             res = lst[a][b][c]

#     print(f"w({a}, {b}, {c}) = {res}")