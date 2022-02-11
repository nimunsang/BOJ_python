# https://www.acmicpc.net/problem/9019

from collections import deque
import sys
input = sys.stdin.readline

def solve(num, target):
    q = deque()
    q.append((num, ""))
    while q:
        n, res = q.popleft()
        if n == target:
            print(res)
            break
        for op in ops:
            if op == 'D':
                dn = (n*2)%10000
                if not visited[dn]:
                    visited[dn] = 1
                    q.append((dn, res+'D'))
            elif op == 'S':
                sn = (n-1)%10000
                if not visited[sn]:
                    visited[sn] = 1
                    q.append((sn, res+'S'))
            elif op == 'L':
                ln = n%1000*10 + n//1000
                if not visited[ln]:
                    visited[ln] = 1
                    q.append((ln, res+'L'))
            elif op == 'R':
                rn = n%10*1000 + n//10
                if not visited[rn]:
                    visited[rn] = 1
                    q.append((rn, res+'R'))


T = int(input())
ops = ['D', 'S', 'L', 'R']
for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000
    solve(A, B)