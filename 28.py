a = input().split()
b = input().split()
res = 0
res1 = 0
  
if (int(a[0]) == int(a[2])):
    res = int(a[0]) + int(a[0]) - int(b[0])
    res1 = int(b[1])
else:
    res1 = int(a[1]) + int(a[1]) - int(b[1])
    res = int(b[0])
print(str(res)+' '+ str(res1))
