import math
  
x1, y1, x2, y2 = map(int,input().split())
x, y, r = map(int,input().split())
cnt = 0
for i in range(max(x1,x-r), min(x2,x+r)+1):
    p =  int(math.sqrt(r**2 - (x - i) ** 2))
    u = min(y + p, y2)
    l = max(y - p, y1)
    cnt += max(u - l + 1, 0)
print(cnt)
