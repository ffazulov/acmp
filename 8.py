user = input()
my_list = user.split()
result1 = int(my_list[2])
x1 = int(my_list[0])
x2 = int(my_list[1])
result2 = x1 * x2
if result1 == result2:
  print('YES')
else:
  print('NO')
