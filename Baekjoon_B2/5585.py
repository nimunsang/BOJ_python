N = 1000 - int(input())

s = 0
lst = [500, 100, 50, 10, 5, 1]

for i in lst:
    cnt = 0
    if (N // i) >= 1:
        cnt = N//i
        s += cnt
        N -= cnt*i
print(s)