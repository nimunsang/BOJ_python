from collections import deque

prices = [1, 2,3 , 2, 3]
answer = deque([])
answer.append(0)
time = 0
while len(prices) != 1:
    p = prices.pop()
    if p < prices[-1]:
        answer.appendleft(time)
    time += 1
    
print(answer)