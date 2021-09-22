n = []

while True:
    m = input()
    if m == '#':
        break
    m = m.replace('-', '0')
    m = m.replace('\\', '1')
    m = m.replace('(', '2')
    m = m.replace('@', '3')
    m = m.replace('?', '4')
    m = m.replace('>', '5')
    m = m.replace('&', '6')
    m = m.replace('%', '7')

    sum = 0
    for i in range(len(m)):
        if m[i] == '/':
            sum -= 8**(len(m)-i-1)
        else:
            sum += int(m[i])* (8**(len(m)-i-1))
    
    print(sum)

