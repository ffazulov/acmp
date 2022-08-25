def qq(n, p):
    s =0
    while n>= p:
        s+=n%p
        n=n//p
    s+=n
    return s
 
n1, p1 = map(int, input().split())
n2, p2 = map(int, input().split())
res = qq(n1, p1)
if res == qq(n2, p2):
    print(res)
else:
    print(0)
