x = [int(i) for i in input().split()]
s = x[0] + x[1] - x[2]
if s >= 0:
  print(s)
else:
  print('Impossible')
