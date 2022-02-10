# https://www.acmicpc.net/problem/11729

def hanoi(k, start, mid, end):
    if k == 1:
        print(start, end)
        return

    hanoi(k-1, start, end, mid)
    print(start, end)
    hanoi(k-1, mid, start, end)



K = int(input())
print(2**K-1)
hanoi(K, 1, 2, 3)
