#다시 #수학
"""
https://www.acmicpc.net/problem/1011
[1011] : Fly me to the Alpha Centauri
"""

import sys
import math

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())

    distance = y - x

    m = math.floor(math.sqrt(distance))
    
    if m == math.sqrt(distance):
        print(2*m - 1)
    
    elif distance <= m**2 + ((m+1)**2 - m**2 - 1)//2:
        print(2*m)
    
    elif distance > m**2 + ((m+1)**2 - m**2 - 1)//2:
        print(2*m+1)