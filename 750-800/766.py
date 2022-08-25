user = input()
user = user.split()
x1 = int(user[0])
x2 = int(user[1])
x3 = int(user[2])
x = x1 * x2
if x < x3:
  print('NO')
else:
  print('YES')
