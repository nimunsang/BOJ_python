K = int(input())

lst = [0, 1]
for i in range(2, K+1):
    lst.append(lst[i-2]+lst[i-1])

print(lst[K-1], lst[K])