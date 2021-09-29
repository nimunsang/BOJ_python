
n = int(input())

m = int(input())
while m != 0:
    if m%n == 0: print("{0} is a multiple of {1}.".format(m, n))
    else: print("{0} is NOT a multiple of {1}.".format(m, n))
    m = int(input())