x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    
for i in range(3):
    if x.count(x[i]) == 1:
        sol_x = x[i]
    if y.count(y[i]) == 1:
        sol_y = y[i]

print("{0} {1}".format(sol_x, sol_y))
