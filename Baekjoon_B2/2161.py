N = int(input())

lst = [i for i in range(1, N+1)]
remove_lst = []

while True:
    i = 0
    if len(lst) == 1:
        print(lst[0])
        break
    remove_lst.append(lst[i])
    print(lst[i], end = " ")
    lst.remove(lst[i])
    lst.append(lst[i])
    lst.remove(lst[i])