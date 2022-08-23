c = 0
k = int(input())
for i in range(1, k+1):
    n = i
    res = 0
    while 0== n%10:
        n//=10
    while n:
        res+= n%10
        res*=10
        n//=10
    res//=10
    if res+i==k:
        c+=1
print(c)
