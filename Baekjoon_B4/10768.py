X = int(input())
Y = int(input())

if(X<2):
    print("Before")
elif(X==2):
    if(Y<=17):
        print("Before")
    elif Y==18:
        print("Special")
    else:
        print("After")
else:
    print("After")