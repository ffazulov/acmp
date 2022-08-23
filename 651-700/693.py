x =[i.lower() for i in input().split()]
flag = True
for i in list(x[0]):
    if i not in list(x[1]):
        flag = False
for i in list(x[1]):
    if i not in list(x[0]):
      flag = False
c1 = 0
for i in x[0]:
  c1 += ord(i)
c2 = 0
for i in x[1]:
  c2 += ord(i)
if flag and c1 ==c2:
    print('Yes')
else:
    print('No')
