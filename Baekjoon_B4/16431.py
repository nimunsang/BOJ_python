Bx, By = map(int, input().split())
Dx, Dy = map(int, input().split())
Jx, Jy = map(int, input().split())

B = abs(abs(Jx-Bx) + abs(Jy-By)) - min(abs(Jx-Bx), abs(Jy-By))
D = abs(abs(Dx-Jx) + abs(Dy-Jy))

if B < D: print("bessie")
elif B==D: print("tie")
else: print("daisy")