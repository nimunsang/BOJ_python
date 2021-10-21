"""
https://www.acmicpc.net/problem/10610
[10610] : 30
"""

N = input()
s = 0
for i in N:
    s += int(i)
if '0' not in N: 
    print("-1")
elif s % 3 != 0:
    print("-1")
else:
    N = list(map(int, N))
    N.sort(reverse = True)
    print(''.join([str(i) for i in N]))