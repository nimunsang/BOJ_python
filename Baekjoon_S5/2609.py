a, b = map(int, input().split())

def GCD(a, b):
    if b%a == 0:
        return a
    elif b%a != 0:
        return GCD(b%a, a)

if a > b: a, b = b, a

print(GCD(a, b))
print(a * b // GCD(a, b))