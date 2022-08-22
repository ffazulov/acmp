a = [int(i)for i in input().split()]
res = list()
for x in range(-100, 101):
    if a[0]*(x**3)+a[1]*(x**2)+a[2]*x+a[3] == 0:
        res.append(x)
for elem in res:
    print(elem, end=' ')
