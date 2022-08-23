a = input()
n = int(a)
r=''
while n > 0:
    y = str(n % 2)
    r = y + r
    n = int(n / 2)
res=0
if (r!=''):
    res = int(r)
for i in range(len(r)):
    r = r[-1] + r[:-1]
    if (res < int(r)):
        res = int(r)
m = int(str(res), 2)
print(m)
