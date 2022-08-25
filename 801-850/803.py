i = 0
a = list(map(int, input().split()))
while i < a[2]:
    a[0] = 10*(a[0] % a[1])
    i=i+1
print(a[0]//a[1])
