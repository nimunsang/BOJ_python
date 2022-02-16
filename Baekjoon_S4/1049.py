# https://www.acmicpc.net/problem/1049

N, M = map(int, input().split())
items = []
for _ in range(M):
    pack, single = map(int, input().split())
    items.append((pack, single))

total = 0
while N:
    packmin, singlemin = 1000, 1000
    if N//6 >= 1:
        for pack, single in items:
            packmin = min(pack, packmin)
            singlemin = min(single, singlemin)

        if packmin < singlemin*6:
            total += packmin
            N -= 6

        else:
            total += singlemin * 6
            N -= 6

    else:
        minimum = 1000
        for pack, single in items:
            minimum = min(minimum, pack, single*N)
        total += minimum
        break

print(total)