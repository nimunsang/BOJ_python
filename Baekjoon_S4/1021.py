#20분 #자료구조 #덱
"""
https://www.acmicpc.net/problem/1021
[1021] : 회전하는 큐
덱의 rotate를 이용하여 풀었다 더 깔끔하게 가능할거같은데
왼쪽회전, 오른쪽회전의 횟수를 비교하여,
작은 횟수를 더해나가는 방식이다
"""

from collections import *

N, M = map(int, input().split())
deq = deque([i for i in range(1, N+1)])
lst = list(map(int, input().split()))

s = 0
for i in lst:
    rcount = 0
    lcount = 0
    
    deq1 = deq.copy()
    deq2 = deq.copy()
    while i != deq1[0]:
        deq1.rotate(1)
        rcount += 1
    while i != deq2[0]:
        deq2.rotate(-1)
        lcount += 1
    if rcount > lcount:
        deq = deq1
        deq.popleft()
        s += lcount
    else:
        deq = deq2
        deq.popleft()
        s += rcount
print(s)