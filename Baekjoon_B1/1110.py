N = int(input())

cnt = 0
num = N
new_num = 0
while True:
    new_num = num%10*10 + (num//10+num%10)%10
    num = new_num
    cnt += 1
    if num == N: break
print(cnt)