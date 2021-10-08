lst = [i for i in range(1, 21)]

for i in range(10):
    a, b = map(int, input().split())
    new_lst = []
    new_lst.extend(lst[:a-1])
    new_lst.extend(reversed(lst[a-1:b]))
    new_lst.extend(lst[b:])
    lst = new_lst

for i in lst:
    print(i, end = " ")