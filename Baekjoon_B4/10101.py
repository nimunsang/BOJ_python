N = []
sum = 0
for i in range(3):
    N.append(int(input()))
    sum += N[i]

if sum != 180:
    print("Error")
else:
    if len(set(N)) == 1:
        print("Equilateral")
    elif len(set(N)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
