#1시간 #구현
"""
https://www.acmicpc.net/problem/14890
[14890] : 경사로
"""

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def checkrow(k):
    lst = []
    for i in range(N):
        lst.append(arr[k][i])
    
    for i in range(N-1):
        if lst[i] != lst[i+1]:
            if abs(int(lst[i]) - int(lst[i+1])) > 1:
                return False
            
            if int(lst[i]) > int(lst[i+1]):
                for j in range(L):
                    if i+1+j == N or int(lst[i+1+j]) != lst[i+1+j] or lst[i+1] != lst[i+1+j]:
                        return False
                
                for j in range(L):
                    lst[i+1+j] += 1/2
            
            elif int(lst[i]) < int(lst[i+1]):
                for j in range(L):
                    if i-j == -1 or int(lst[i-j]) != lst[i-j] or lst[i] != lst[i-j]:
                        return False
                
                for j in range(L):
                    lst[i-j] += 1/2
    return True
            

def checkcol(k):
    lst = []
    for i in range(N):
        lst.append(arr[i][k])
    
    for i in range(N-1):
        if lst[i] != lst[i+1]:
            if abs(int(lst[i]) - int(lst[i+1])) > 1:
                return False
            
            if int(lst[i]) > int(lst[i+1]):
                for j in range(L):
                    if i+1+j == N or int(lst[i+1+j]) != lst[i+1+j] or lst[i+1] != lst[i+1+j]:
                        return False
                
                for j in range(L):
                    lst[i+1+j] += 1/2
            
            elif int(lst[i]) < int(lst[i+1]):
                for j in range(L):
                    if i-j == -1 or int(lst[i-j]) != lst[i-j] or lst[i] != lst[i-j]:
                        return False
                
                for j in range(L):
                    lst[i-j] += 1/2
    return True


ans = 0
for i in range(N):
    if checkrow(i):
        ans += 1
    if checkcol(i):
        ans += 1
print(ans)
