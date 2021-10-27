#10분 #구현 #문자열 #브루트포스 알고리즘
"""
https://www.acmicpc.net/problem/1120
[1120] : 문자열
"""

A, B = input().split()

complst = []
for i in range(len(B)-len(A)+1):
    s = 0
    compB = B[i:i+len(A)]
    for j in range(len(A)):
        if A[j] == compB[j]:
            s += 1
    complst.append(s)
    
print(len(A) - max(complst))