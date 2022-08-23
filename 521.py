res = 0
p, k = map(int, input().split())
for i in range(p, k+1):
  t = i
  while t!=2:
    if t%2:
      t= t*3+1
    else:
      t//=2
    res+=1
print(res)
