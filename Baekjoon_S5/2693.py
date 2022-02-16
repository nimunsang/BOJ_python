# https://www.acmicpc.net/problem/2693

T = int(input())
for _ in range(T):
    print(sorted(list(map(int, input().split())), reverse = True)[2])