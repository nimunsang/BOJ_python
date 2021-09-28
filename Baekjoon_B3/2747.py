n = int(input())

f = [0, 1]
for i in range(n):
    f.append(f[i]+f[i+1])

print(f[n])