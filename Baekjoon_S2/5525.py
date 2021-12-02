#20분 #문자열
"""
https://www.acmicpc.net/problem/5525
[5525] : IOIOI
"""

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

cnt = 0
ans = 0
i = 1

while i+1 < M:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        cnt += 1
        if cnt == N:
            ans += 1
            cnt -= 1
        i += 1
    
    else:
        cnt = 0

    i += 1

print(ans)


# =====첫 시도=====
# target = "IO"*(N)+"I"
# length = len(target)

# ans = 0
# for i in range(M - length):
#     if S[i:i+length] == target:
#         ans += 1

# print(ans)