#다시
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    ind = list(range(N))
    target = ind[M]

    cnt = 0
    while True:
        if imp[0] == max(imp):
            cnt += 1
            if ind[0] == target:
                break

            else:
                imp.pop(0)
                ind.pop(0)
        else:
            imp.append(imp.pop(0))
            ind.append(ind.pop(0))
            
    print(cnt)