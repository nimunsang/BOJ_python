import sys
input = sys.stdin.readline

N = int(input())

lst = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    lst.append((i, age, name))

lst.sort(key= lambda x:(x[1], x[0]))

for i, a, n in lst:
    print(a, n)