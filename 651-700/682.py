n = int(input())
if n ==1:
  print(45)
else:
  if n==2:
    print(4905)
  else:
    print(494, end='')
    for i in range(n-3):
      print(9, end='')
    print(55, end='')
    for i in range(n-2):
      print(0, end='')
