#다시
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

while start <= end:
    mid = (start+end) // 2
    s = 0
    for tree in trees:
        if tree > mid:
            s += tree - mid
        
        if s >= M:
            start = mid + 1
        else:
            end = mid - 1
print(end)



