b = int(input())
if b==1 or b==2 or b==3 or b==6:
  print(-1)
  exit()
if b ==4:
  print(2,1,0,1, sep='\n')
  exit()
if b ==5:
  print(1,2,0,0,2, sep='\n')
  exit()
a = [0 for i in range(b+1)]
a[1] = 2
a[2] = 1
a[b-4] = 1
a[b] = b-4
for i in range(1, len(a)):
  print(a[i])
