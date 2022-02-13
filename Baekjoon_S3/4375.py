#2분 #수학 #브루트포스알고리즘 #정수론
"""
https://www.acmicpc.net/problem/4375
[4375] : 1
"""

while True:
    try:
        N = int(input())
        i = 1
        while int('1'*i) % N :
            i += 1

        print(i)

    except:
        break
