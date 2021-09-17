import sys

N = int(input())
t = list(map(int, input().split()))
y_sum = 0
m_sum = 0
for i in range(N):
    
    sec = t[i] % 60
    y_sum += t[i] // 60 * 20
    m_sum += t[i] // 60 * 15
    if sec <= 29: 
        y_sum += 10
        m_sum += 15
    elif sec <= 59:
        y_sum += 20
        m_sum += 15
    
if y_sum == m_sum: print("Y M {0}".format(y_sum))
elif y_sum > m_sum: print("M {0}".format(m_sum))
else: print("Y {0}".format(y_sum))