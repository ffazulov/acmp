a = input()
k = int(input())
res = str()
if k>0:
  for i in range(1,1024):
    res+=a
    if i==k:
      break
else:
  k = abs(k)
  if a.count(a[0: int(len(a)/k)]) == k and len(a)%k == 0:
    res = a[0: int(len(a)/k)]
  else:
    res = 'NO SOLUTION'
print(res[0:1023])
