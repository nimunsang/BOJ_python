s = input()

sum = 10
for i in range(len(s)-1):
    if s[i] == '(':
        if s[i+1] == '(':
            sum += 5
        else:
            sum += 10
    elif s[i] == ')':
        if s[i+1] == '(':
            sum += 10
        else:
            sum += 5
print(sum)