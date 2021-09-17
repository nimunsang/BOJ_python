# ============처음 생각한 답===========
# 시간초과로 실패..

# T = int(input())
# lst = []
# for i in range(T):
#     a, b = map(int, input().split())
#     lst.append(a**b%10)

# for i in range(T):
#     print(lst[i])

T = int(input())
result = []

for _ in range(T):
    a, b = map(int, input().split())
    if a%10 == 0: 
        result.append(10)
        continue

    temp = 1
    lst = [] # 반복되는 나머지
    for _ in range(b):
        temp = temp * a % 10 # 10번을 제외하면, 일의 자리만 쓸모있다
        if(temp in lst):
            break
        lst.append(temp)

    result.append(lst[b%len(lst)-1])

for i in range(T):
    print(result[i])
