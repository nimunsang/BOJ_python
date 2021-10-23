#6분..
"""
https://www.acmicpc.net/problem/11653
[11653] : 소인수분해
"""
N = int(input())

i = 2
while True:
    if N%i == 0:
        print(i)
        N = N // i
    else:
        i += 1
    
    if N == 1:
        break