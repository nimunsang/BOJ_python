import re

T = int(input())

for _ in range(T):
    s = input()
    print("Infected!" if re.fullmatch('[A-F]?[A]+[F]+[C]+[A-F]?', s) else "Good")
