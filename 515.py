import math
n = int(input())
l_x = [0]
l_y = [0]
for i in range (n):
    x, y = map(int,input().split())
    l_x.append(x)
    l_y.append(y)
d = 0
for i in range (n):
    d += math.sqrt((l_x[i+1]-l_x[i])**2+(l_y[i+1]-l_y[i])**2)
d += math.sqrt((l_x[-1]-l_x[0])**2+(l_y[-1]-l_y[0])**2)
print(d)
