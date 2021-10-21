N = input()

lst = [0 for _ in range(10)]

for i in range(len(N)):
    lst[int(N[i])] += 1

if lst[6]+lst[9] >= 2:
    if (lst[6]+lst[9]) % 2 == 0:
        lst[6] = lst[9] = (lst[6]+lst[9])//2
    else:
        lst[6] = lst[9] = (lst[6]+lst[9])//2 + 1

print(max(lst))
