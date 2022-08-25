x = [int(i) for i in input().split()]
ma = x[-1]
for i in x:
  if i <94 or i>727:
    print('Error')
    ma = ''
    break
  else:
    if ma<i:
      ma = i
print(ma)
