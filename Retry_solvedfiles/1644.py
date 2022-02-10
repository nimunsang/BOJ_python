# https://www.acmicpc.net/problem/1644

import math
N = int(input())

maximum = N
sosu = [1] * (maximum+1)
sosulist = [0]
for i in range(2, int(math.sqrt(maximum))+1):
    for j in range(2*i, maximum+1, i):
        sosu[j] = 0

for i in range(2, maximum+1):
    if sosu[i]:
        sosulist.append(i)

length = len(sosulist)
for i in range(1, length):
    sosulist[i] += sosulist[i-1]

start = 0
end = 1
cnt = 0
while end < length:
    res = sosulist[end]-sosulist[start]
    if res == N:
        cnt +=1 
        end += 1
    else:
        if res < N:
            end += 1
        else:
            start += 1

print(cnt)