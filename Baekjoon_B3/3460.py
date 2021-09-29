T = int(input())

for i in range(T):
    n = int(input())
    s = bin(n)[2:] 

    lst = list(s)
    lst.reverse()

    for j in range(len(lst)):
        if lst[j] == "1":
            print(j, end = " ")
    print("")