#N: 총카드 // M: O // N-M: X // K: O를 적은 개수 // N-K: X를 적은개수
N, M, K = map(int, input().split())

#앞면과 뒷면에 같은모양이 적힌 최대 개수..
# O: 3개 X: 1개
# O: 2개 X: 2개

# O: 3 X: 2
# O: 3 X: 2

print(min(M, K) + min(N-M, N-K))