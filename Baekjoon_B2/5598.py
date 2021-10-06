s = input()

for i in s:
    if 'D' <= i <= 'Z': print(chr(ord(i)-3), end = "")
    else: print(chr(ord(i)+23), end = "")