cr = 3
s =0
n = int(input())
a = [int(i) for i in input().split()]
for i in range(n):
    if a[i]:
        s+=cr
        cr+=1
    else:
        cr-=3
        if cr<3:
            cr = 3
print(s)
