#30분 #브루트포스알고리즘
"""
https://www.acmicpc.net/problem/1107
[1107] : 리모컨
"""

N = int(input())
M = int(input())
if M != 0: 
    broken = list(map(int, input().split()))
else:
    broken = []
    
answer = abs(100 - N)

for num in range(1000000):
    for n in str(num):
        if int(n) in broken:
            break
    else:
        answer = min(answer, len(str(num)) + abs(num - N))
        
print(answer)