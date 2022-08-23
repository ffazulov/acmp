a = [int(i) for i in input().split()]
r = 2 * (a[0] + a[1]) * a[2]
re = r%16
r = r //16
if re == 0:
  print(r)
else:
  print(r+1)
