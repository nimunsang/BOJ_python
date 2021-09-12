N = int(input())

min = N//60
sec = N % 60
A = min // 5
B = min % 5
C = sec // 10

if sec % 10 == 0: print("{0} {1} {2}".format(A, B, C))
else: print("-1")