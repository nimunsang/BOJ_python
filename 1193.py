X = int(input())

cnt = 1
while True:
    if X in range(cnt*(cnt-1)//2, cnt*(cnt+1)//2+1):
        break
    cnt += 1

ind = X - cnt*(cnt-1)//2

if cnt % 2 == 0:
    print("{0}/{1}".format(ind, cnt-ind+1))
else:
    print("{0}/{1}".format(cnt-ind+1, ind))