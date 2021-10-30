#10분 #다이나믹프로그래밍
#피보나치 수열로 증가하는 것을 확인하였다.
#n이 너무 커지면, 게산 시간이 너무 오래걸리므로,
#배열에 미리 저장하는 식으로 코드를 짰다.
"""
https://www.acmicpc.net/problem/11726
[11726] : 2xn 타일링
"""

def sol(n, ar):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        ar[1] = 1
        ar[2] = 2
        for i in range(3, n+1):
            ar[i] = ar[i-1] + ar[i-2]
    
    return ar[n]


n = int(input())
arr = [0] * (n+1)
print(sol(n, arr)%10007)