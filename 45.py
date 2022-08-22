n = int(input())
if 0==n:
    print(10)
    exit()
if n ==1:
    print(1)
    exit()
a = [0 for i in range(10)]
for i in range(9, 1, -1):
    while not (n%i):
        n/=i
        a[i]+=1
if n==1:
    for i  in range(2,10):
        while a[i]:
            a[i]-=1
            print(i, end='')
else:
    print(-1)
