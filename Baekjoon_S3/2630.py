N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

def cut(arr, n):
    global blue
    global white

    a, b, c, d = [], [], [], []

    for i in range(n//2):
        a.append(arr[i][:n//2])
        b.append(arr[i][n//2:n])
        c.append(arr[n//2+i][:n//2])
        d.append(arr[n//2+i][n//2:n])
    
    lst = [a, b, c, d]

    for l in lst:
        white_cnt = 0
        blue_cnt = 0
    
        for i in l:
            white_cnt += i.count(0)
            blue_cnt += i.count(1)

        if white_cnt == 0:
            blue += 1
        elif blue_cnt == 0:
            white += 1
        else:
            cut(l, n//2)



white = 0
blue = 0
for i in arr:
    white += i.count(0)
    blue += i.count(1)

if white == N**2:
    print("1")
    print("0")
elif blue == N**2:
    print("0")
    print("1")

else:
    white = 0
    blue = 0
    cut(arr, N)
    print(white)
    print(blue)