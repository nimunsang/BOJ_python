T = int(input())

for i in range(T):
    num = int(input())
    quarter, dime, nickel, penny = 0, 0, 0, 0
    if num // 25 >= 1:
        quarter += num//25
        num %= 25
    if num // 10 >= 1:
        dime += num//10
        num %= 10
    if num // 5 >= 1:
        nickel += num // 5
        num %= 5
    penny += num

    print("{0} {1} {2} {3}".format(quarter, dime, nickel, penny))


