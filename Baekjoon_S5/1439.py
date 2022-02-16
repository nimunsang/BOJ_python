# https://www.acmicpc.net/problem/1439

S = input()

a, b = 0, 0
if S[0] == '0':
    a += 1
else:
    b += 1
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        if S[i] == '0':
            a += 1
        else:
            b += 1

if a == 0 or b == 0:
    print(0)
else:
    print(min(a, b))

