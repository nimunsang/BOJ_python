A, B, C = map(int, input().split())
money = 0
if (A==B==C):
    money = 10000 + A*1000
elif (A!=B) & (B!=C) & (A!=C):
    money = max(A, B, C) * 100
else:
    if (A==B) | (A==C):
        money = 1000 + A * 100
    else:
        money = 1000 + B * 100

print(money)