n = int(input())
a = [int(i) for i in input().split()]
v = int(input())
b = {}
for i in range(v):
    k = [int(i) for i in input().split()]
    b[k[0]] = k[1]
 
for i in range(len(a)):
    if a[i] in b:
        print(b[a[i]], end=' ')
    else:
        print(a[i], end=' ')
