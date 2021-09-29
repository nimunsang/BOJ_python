T = int(input())

for i in range(T):
    s = int(input())
    n = int(input())
    for j in range(n):
        p, q = map(int, input().split())
        s += p*q
    print(s)