import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    K = int(input())

    tri = []
    i = 1
    while True:
        tri.append(i*(i+1)//2)
        if tri[i-1] >= K:
            break
        i+=1

    l = len(tri)
    mask = 0
    for i in range(l):
        if mask == 1: break
        for j in range(l):
            if mask == 1: break
            for m in range(l):
                if tri[i]+tri[j]+tri[m] == K:
                    mask = 1
                    break
    
    print(mask)