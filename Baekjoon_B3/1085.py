x, y, w, h = map(int, input().split())

x_min = min(abs(x-w), x)
y_min = min(abs(y-h), y)

print(min(x_min, y_min))

# print(min(x, y, w-x, h-y))