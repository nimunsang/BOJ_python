arr = []

def star(num) :
    global arr

    if num > 1 : 
        star(num//3)

    for i in range(len(arr)) :
        for j in range(len(arr)) :
           if i//num%3==1 and j//num%3==1 :
               arr[i][j] = " "


num = int(input())

str = []
for i in range(num) :
    str.append("*")
for i in range(num) :
    arr.append(str)

star(num//3)

for i in range(num) :
    for j in range(num) :
        print("%c" % (arr[i][j]), end = "")
    print()