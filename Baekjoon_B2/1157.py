S = input().upper()

lst = [0 for _ in range(26)]
for i in S:
    lst[ord(i)-65] += 1

if lst.count(max(lst)) > 1:
    print("?")
else:
    max = 0
    max_s = ''
    for i in S:
        if lst[ord(i)-65] > max:
            max = lst[ord(i)-65]
            max_s = i
    print(max_s)