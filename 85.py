n,m = map(int, input().split())
while n*m != 0 :
    if n>m:
        n=n%m
    else:
        m = m%n
if n==0:
    n=m
for z in range(n):
    print(1, end='')
