x = [int(i) for i in input().split()]
count = 0
for i in range(x[0], x[1] + 1):
  pr = 1
  list_sp = [int(h) for h in list(str(i))]
  for j in list_sp:
    pr = pr * j
  if pr == 0:
    continue
  elif i%pr == 0:
    count += 1
print(count)
