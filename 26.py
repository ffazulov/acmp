x1, y1, r1 = map(int,input().split())
x2, y2, r2 = map(int,input().split())
distance = ((x2-x1)**2+(y2-y1)**2)**0.5
  
if (distance<=r1 + r2) and (r1+r2>=distance) and (distance+r2>=r1) and (distance+r1>=r2):
    print('YES')
else:
    print('NO')
