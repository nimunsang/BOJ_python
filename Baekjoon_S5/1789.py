"""
https://www.acmicpc.net/problem/1789
[1789] : 수들의 합
"""

S = int(input())
i = 1
while True:
    if S in range((i*(i+1)//2), ((i+1)*(i+2)//2)):
        print(i)
        break
    else:
        i += 1