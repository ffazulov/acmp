x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
if abs(x1-x2)==abs(y1-y2):
    print(1)
else:
    if (x1+y1)%2==(x2+y2)%2:
        print(2)
    else:
        print(0)
