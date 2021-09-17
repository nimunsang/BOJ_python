# ============답은 맞게 나오는데 시간초과===========

# N = int(input())

# lst = []
# result = []
# while N != 0:
#     lst.append(N%10)
#     N = N // 10

# for i in lst:
#     index = 0
#     bin_lst = [0, 0, 0]
#     while i != 0:
#         if i % 2 == 1:
#             bin_lst[index] = 1
#         i = i//2
#         index += 1
    
#     result += bin_lst

# for i in range(1, len(result)+1):
#     if (i == 1) & (result[len(result) - i] == 0):
#         continue
#     print(result[len(result) - i], end = "")

# ==============내 2번째 풀이.. 시간초과 ==============
# N = input()
# mystr = ""
# for i in range(len(N)):
#     lst = [0, 0, 0]
#     n = int(N[i])
#     cnt = 0   
#     while(n != 0):
#         if n%2 == 1:
#             lst[2-cnt] = 1
#         n = n // 2
#         cnt += 1
#     for k in lst:
#         mystr += str(k)


# if mystr[0] == '0':
#     mystr = mystr[1:]
# print(int(mystr))


print(bin(int(input(), base = 8))[2:])
# base = 8 : 입력받은 정수를 8진수로 바꿔줌!