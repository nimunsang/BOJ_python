A, B, V = map(int, input().split())

tmp = A-B
day = (V-A)//tmp 
snail = tmp*day
while True:
    day += 1
    snail += A
    if snail >= V:
        print(day)
        break
    snail -= B