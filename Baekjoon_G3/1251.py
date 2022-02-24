S = input()
ord1 = S.index(chr(min(map(lambda x: ord(x), S))))
ord2 = S.index(chr(min(map(lambda x: ord(x), S[:ord1]+S[ord1+1:]))))
print(S[:ord1+1][::-1] + S[ord1+1:ord2+1][::-1] + S[ord2+1:][::-1])
