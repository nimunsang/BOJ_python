import sys
input = sys.stdin.readline

N = int(input())

lst = []
for i in range(N):
    lst.append(input().rstrip())

same = list(lst[0])
for i in range(1, N):
    for j in range(len(same)):
        if same[j] != lst[i][j]:
            same[j] = '?'
            
print(''.join(same))