m=0
n=int(input())
a=list(map(int,input().split()))
for i in range (n):
    if(a[i]<a[m]):
        m=i
for i in range(m,n):
    print(a[i])
for i in range (m):
    print(a[i])
