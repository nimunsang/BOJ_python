N, L, D = map(int, input().split())

time = D
min = L
max = L+5
temp = L+5
while(True):
    while time < min:
        time += D
   # print("time : {0} , min~max : {1}~{2}".format(time, min, max))
    if time in range(min, max):

        print(time)
        break

    if time >= L*N + 5*(N-1):
        print(time)
        break

    min += temp
    max += temp