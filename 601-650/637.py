n = int(input())
a = [int(i) for i in input().split()]
s = 0
k = int(input())
for i in range(n):
    if a[i]>k:
        s+=k
    else:
        s+=a[i]
print(s)
