i = list(str(input()))
count = 0
for el in i:
  if el == '0':
    count += 1
if count == 0:
  print('YES')
else:
  print('NO')
