"""
https://www.acmicpc.net/problem/1002
[1002] : 터렛
"""

import sys
input = sys.stdin.readline

from math import *

T = int(input())

for i in range(T):
    lst = list(map(int, input().split()))
    # 두 원의 좌표가 같고, 반지름이 같으면 무한
    if lst[0] == lst[3] and lst[1] == lst[4] and lst[2] == lst[5]:
        print("-1")
    # 작은 원의 반지름과 두 원 사이의 거리의 합이 큰 원의
    # 반지름 보다 작을 때, 두 원은 만나지 않는다
    elif (sqrt((lst[3]-lst[0])**2 + (lst[4]-lst[1])**2)) \
        + min(lst[2], lst[5]) < max(lst[2], lst[5]):
        print("0")
    # 작은 원이 큰 원에 내접하는 경우
    elif (sqrt((lst[3]-lst[0])**2 + (lst[4]-lst[1])**2)) \
        + min(lst[2], lst[5]) == max(lst[2], lst[5]):
        print("1")
    # 두 원이 두 점에서 만나는 경우
    elif sqrt((lst[3]-lst[0])**2 + (lst[4]-lst[1])**2) \
        < (lst[2]+lst[5]):
        print("2")
    # 두 원이 외접하는 경우
    elif sqrt((lst[3]-lst[0])**2 + (lst[4]-lst[1])**2) \
        == (lst[2]+lst[5]):
        print("1")
    else:
        print("0")