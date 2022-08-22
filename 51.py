s = input()
a = s.split(' ')
b = len(a[1])
res = 1
  
if ((int(a[0])%b)==0):
    c = int(a[0])
    while (c>0):
        res = res * c
        c = c - b
else:
    c = int(a[0])
    while (c > (int(a[0])%b)):
        res = res * c
        c = c - b
    res = res * (int(a[0])%b)
print(res)
