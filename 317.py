x, y, z, w = map(int, input().split())
count = 0
for i in range(0, w // x + 1):
    rest = w - x * i
    for j in range(0 , rest // y + 1):
        if (rest - y * j) % z == 0:
            count += 1
print(count)
