N = int(input())
num = 2**((-1)*N)
ans = ""
if str(num).find('e') == -1:
    print(num)

else:
    index = str(num).find('e')
    a = str(num)[0:index]
    b = str(num)[index+2:]

    ans += "0."
    for i in range(int(b)-1):
        ans += '0'
    ans += str(num)[0] + str(num)[2:index]
    print(ans)