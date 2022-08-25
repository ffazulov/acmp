def func(n, k):
    s = 0
    while n >=k:
        s+=n%k
        n//=k
    s+=n
    return s
 
n,k,k1 = map(int, input().split())
a = [i for i in range(n)]
t = [int(i) for i in input().split()]
for i in range(len(t)):
    a[i] = func(t[i],k)*func(t[i],k1)
for i in sorted(a):
    print(i, end=' ')
