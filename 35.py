k = int(input())
for i in range(k):
  user = input()
  listx = user.split()
  n = int(listx[0])
  m = int(listx[1])
  d = 19*m+(n+239)* (n + 366) / 2
  print(round(d))
