import sys
input = sys.stdin.readline
N, K = map(int, input().split())

lst_boy = []
lst_girl = []
for i in range(N):
    S, Y = map(int, input().split())
    if S == 0: lst_girl.append(Y)
    else: lst_boy.append(Y)

room = 0
for i in range(1, 7):
    if lst_boy.count(i) % K == 0:
        room += lst_boy.count(i) // K
    else:
        room += lst_boy.count(i) // K + 1
    if lst_girl.count(i) % K == 0:
        room += lst_girl.count(i) // K
    else:
        room += lst_girl.count(i) // K + 1
print(room)