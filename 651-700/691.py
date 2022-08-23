import re
x = int(input())
teg = r'[ABCEHKMOPTXY][0-9]{3}[ABCEHKMOPTXY]{2}'
for i in range(x):
  c = input()
  if re.fullmatch(teg, c):
    print('Yes')
  else:
    print('No')
