#해결 #그래프이론 #그래프탐색 #너비우선탐색
"""
https://www.acmicpc.net/problem/9019
[9019] : DSLR
"""

from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    q = deque()
    q.append([a, ""])
    while q:
        num, ans = q.popleft()
        dn = (num * 2) % 10000
        if arr[dn] == 0:
            if dn == b:
                return ans + "D"
            else:
                arr[dn] = 1
                q.append([dn, ans + "D"])
        
        sn = num-1
        if sn < 0:
            sn += 10000
        if arr[sn] == 0:
            if sn == b:
                return ans+ "S"
            else:
                arr[sn] = 1
                q.append([sn, ans + "S"])
        
        ln = (num%1000)*10 + num//1000
        if arr[ln] == 0:
            if ln == b:
                return ans+ "L"
            else:
                arr[ln] = 1
                q.append([ln, ans+ "L"])
        
        rn = (num%10)*1000 +(num//10)
        if arr[rn] == 0:
            if rn == b:
                return ans+ "R"
            else:
                arr[rn] = 1
                q.append([rn, ans+ "R"])
        
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    arr = [0] * 10000
    print(bfs(A, B))