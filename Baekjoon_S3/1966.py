#해결 #구현 #자료구조 #시뮬레이션 #큐
"""
https://www.acmicpc.net/problem/1966
[1966] : 프린터 큐
"""

from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # implist : 중요도를 나타내는 리스트
    implist = deque(list(map(int, input().split())))
    # target : 타겟으로 설정한 중요도
    target = implist[M]
    
    # indexlist : 처음 입력으로 들어온 리스트의 index 저장
    indexlist = deque(list(range(N)))

    cnt = 1
    while True:
        if implist[0] == max(implist):

            if indexlist[0] == M:
                print(cnt)
                break

            else:
                implist.popleft()
                indexlist.popleft()
                cnt += 1
            
        else:
            implist.rotate(-1)
            indexlist.rotate(-1)