n = int(input())

fibo = [0, 1]
i = 0
while True:
    fibo.append(fibo[i] + fibo[i+1])
    i += 1
    if i == n: 
        print(fibo[n])
        break

print(fibo)