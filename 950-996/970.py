x = [int(i) for i in input().split()]
if x[0] + x[1]==x[2] or x[0] + x[2]==x[1] or x[2] + x[1]==x[0]:
  print('YES')
else:
  print('NO')
