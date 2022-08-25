x = [int(i) for i in input().split()]
q = x[0]*x[1]
res = q**(1/2)
if res-int(res)==0:
  print(int(res))
else:
  print(0)
