N, B = map(int, input().split())

lst = []
while True:
    lst.append(N%B)
    N //= B

    if N == 0: break
s = ""
for i in lst:
    if i >= 10:
        s += chr(i+55)
    else:
        s += str(i)

print(s[::-1])