"""
https://www.acmicpc.net/problem/4796
[4796] : 캠핑
"""
case = 1
while True:
    L, P, V = map(int, input().split())
    if (L, P, V) == (0, 0, 0):
        break
    else:
        if V%P > L:
            print(f"Case {case}: {L*(V//P)+L}")
        else:
            print(f"Case {case}: {L*(V//P)+(V%P)}")
        case += 1