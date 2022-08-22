k = [int(i) for i in input().split()]
y = 0
for i in range (1000):
    y = k[0]-i
    if (i <= y and i*y == k[1]):
        print(i,y)
        break
