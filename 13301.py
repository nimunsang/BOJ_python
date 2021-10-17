N = int(input())

lst = [1, 1]
if N == 1:
    print(4)
else:
    for i in range(2, N):
        lst.append(lst[i-2] + lst[i-1])

    print(lst[N-1]*4 + 2 * lst[N-2])