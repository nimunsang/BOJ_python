lst = []
for i in range(10):
    lst.append(int(input()))

s_0 = 0
s_1 = 0
for i in range(10):
    s_0 += lst[i]
    if s_0 > 100:
        s_1 = s_0
        s_0 = s_0 - lst[i]
        break

if s_1 == 0: print(s_0)
else:
    if (s_1-100) > (100-s_0): print(s_0)
    elif (s_1-100) == (100-s_0): print(s_1)
    else: print(s_1)