import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    
    arr = list(map(int, input().split()))
    arr = list(map(lambda x: (x[0]+1,x[1]), enumerate(arr)))
    
    visited = [0]*(N+1)
    cnt = 0
    for a, b in arr:
        if visited[a] == 0:
            cnt += 1
            visited[a] = cnt
            visited[b] = cnt
        
        else:
            visited[b] = visited[a]
    print(visited)