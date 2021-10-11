s = input()

while s != '0':
    if s == s[::-1]: print("yes")
    else: print("no")
    s = input()