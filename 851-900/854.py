f = [int(i) for i in input().split()]
a = input()
if a == 'heat':
  if f[0] <f[1]:
    print(f[1])
  else:
    print(f[0])
elif a == 'freeze':
  if f[0] <f[1]:
    print(f[0])
  else:
    print(f[1])
elif a == 'fan':
  print(f[0])
elif a == 'auto':
  print(f[1])
