sum1 = 0
sum2 = 0
for i in range(4):
  user = input()
  my_list = user.split()
  sum1 = sum1 + int(my_list[0])
  sum2 += int(my_list[1])
if sum1 > sum2:
  print('1')
if sum1 < sum2:
  print('2')
if sum1 == sum2:
  print('DRAW')
