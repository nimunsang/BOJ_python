import sys
input = sys.stdin.readline

lst = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

a = input()
num = 0

for i in a:
    for j in lst:
        if i in j:
            num += lst.index(j) + 3

print(num)