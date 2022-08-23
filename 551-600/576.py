def qq(a, b):
    c = 0
    while b:
        c = a
        a = b
        b = c%a
    if a==1:
        return 1
    else:
        return 0
 
n,a,k = 0,0,0
n= int(input())
a = n-1
while a:
    if qq(a,n):
        k+=1
    a-=1
print(k)
