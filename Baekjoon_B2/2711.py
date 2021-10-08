T = int(input())

for i in range(T):
    a, b = input().split()
    a = int(a)
    b = list(b)
    s = ""
    b.pop(a-1)
    for j in b:
        s += j
    print(s)

# =====두번째=====
# T = int(input())

# for i in range(T):
#     a, b = input().split()
#     a = int(a)
#     print(b[:a-1] + b[a:])