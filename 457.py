i = 0
a = [0 for _ in range(4)]
n = int(input())
while 1:
    n1 = n
    a[0] = n//1000
    a[1] = n // 100%10
    a[2] = n//10%10
    a[3] = n%10
    a = sorted(a)
    t2 = a[0]*1000+a[1]*100+a[2]*10+a[3]
    t1 = a[3] * 1000 + a[2] * 100 + a[1] * 10 + a[0]
    n1 = t1-t2
    i+=1
    if n1==n:
        break
    n=n1
print(n)
print(i-1)
