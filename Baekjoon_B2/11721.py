N = input()

for i in range(len(N)):
    print(N[i], end = "")
    if i % 10 == 9:
        print("")