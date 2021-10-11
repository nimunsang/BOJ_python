s = input()

for i in s:
    if ord(i) in range(97, 110) or ord(i) in range(65, 78):
        print(chr(ord(i)+13), end = "")
    elif ord(i) in range(110, 123) or ord(i) in range(78, 91):
        print(chr(ord(i)-13), end = "")
    else:
        print(i, end = "")