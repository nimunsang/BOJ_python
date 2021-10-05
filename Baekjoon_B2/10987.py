s = input()

lst = "aeiou"
cnt = 0
for i in s:
    if i in lst:
        cnt += 1
print(cnt)