lst = [int(input()) for i in range(10)]

print(sum(lst)//10)
print(max(lst, key= lst.count))