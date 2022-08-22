user = 'qwertyuiopasdfghjklzxcvbnm'
user = list(user)
x = input()
k = user.index(x)
if k == 25:
  print(user[0])
else:
  print(user[k+1])
