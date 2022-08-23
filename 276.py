a, b = map(int, input().split())
 
c = a-a//b*b
for i in range(b-c):
    print(a//b, end=' ')
for i in range(c):
    print(a//b+1, end=' ')
