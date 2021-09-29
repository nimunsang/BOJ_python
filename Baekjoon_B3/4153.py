l = list(map(int, input().split()))
l.sort()

while not(l[0]==0 and l[1]==0 and l[2]==0):
    if (l[0]**2 + l[1]**2) == l[2]**2:
        print("right")
    else:
        print("wrong")
    l = list(map(int, input().split()))
    l.sort()