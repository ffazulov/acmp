n = int(input())
res = 1
a = 1
c = 0
for i in range (1,n+1):
    if (n % i == 0):
        b = str(i)
        for j in range (len(b)):
            c = c + int(b[j])
        if (c > a):
            res=i
            a = c
            c = 0
        else:
            c = 0
if (res == 1):
    print(n)
else:
    print(res)
