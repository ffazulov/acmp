n,w,d,p = map(int, input().split())
s = 0
for i in range(1, n):
  s+=i*w
if s==p:
  print(n)
else:
  print(abs(p-s)//d)
