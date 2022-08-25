x = int(input())
n, a, b, c = map(int,input().split())
  
if x == 2:
    print(min(a, b, c))
else:
    e = (a + b + c) - (n * 2)
  
    if e < 0:
        print(0)
    else:
        print(e)
